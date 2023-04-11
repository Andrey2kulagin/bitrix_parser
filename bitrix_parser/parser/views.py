from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from .forms import StopWordsForm, RefreshIntervalForm, BitrixAccountDataForm
from .models import User, StopWords, RefreshInterval, BitrixAccountData
from .parser import is_account_data_valid
from django.shortcuts import redirect


@login_required(login_url='login')
def index(request):
    stop_words = StopWords.objects.filter(user=request.user)
    try:
        refresh_interval = RefreshInterval.objects.get(user=request.user)
        print(refresh_interval)
        refresh_interval_data = {"start": refresh_interval.start, "end": refresh_interval.end}
    except:
        refresh_interval_data = {"start": 1, "end": 5}
    try:
        bitrix_account_data = BitrixAccountData.objects.get(user=request.user)
        bitrix_interval_data = {"login": bitrix_account_data.login, "password": bitrix_account_data.password}
    except:
        bitrix_interval_data = {}
    context = {
        "BitrixAccountDataForm": BitrixAccountDataForm(initial=bitrix_interval_data),
        "refresh_interval_form": RefreshIntervalForm(initial=refresh_interval_data),
        "stop_words_form": StopWordsForm(),
        "stop_words": stop_words,
    }
    if request.method == "POST":
        index_post_processing(request)
    return render(request, "parser/index.html", context)


def index_post_processing(request):
    post = request.POST
    name = post.get("form_type")
    if name == "stop_words":
        add_stop_word(request)
    if name == "bitrix_data":
        add_bitrix_data(request)
    if name == "interval_data":
        add_change_refresh_interval(request)
    if name == "del_stop_words":
        del_stop_word(request)


@login_required(login_url='login')
def bitrix_data_submit(request):
    context = {
    "BitrixAccountDataForm": BitrixAccountDataForm()
    }
    if request.method == "POST":
        form = BitrixAccountDataForm(request.POST)
        if form.is_valid():
            login = request.POST.get("login")
            password = request.POST.get("password")
            BitrixAccountData(login=login, password=password, user=request.user).save()
            if is_account_data_valid(login, password):
                user = request.user
                user.is_auth = True
                user.save()
                return redirect('index')
            else:
                context["errors"] = "Не удалось произвсти вход. Если данные точно верны, попробуйте ещё раз"
        else:
            context["errors"] = form.errors
    return render(request, "parser/bitrix_data_submit.html", context)


def start_parser(request):
    user = request.user
    if user.is_auth:
        interval = RefreshInterval.objects.get(user=user)
        bitrix_data = BitrixAccountData.objects.get(user=user)
        stop_words = [i.word for i in StopWords.objects.filter(user=user)]
        interval_start = interval.start
        interval_end = interval.end
        bitrix_login = bitrix_data.login
        bitrix_password = bitrix_data.password


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "parser/login.html"

    def get_success_url(self):
        if self.request.user.is_auth:
            return reverse_lazy('index')
        else:
            return reverse_lazy('bitrix_data_submit')

    def form_valid(self, form):
        user = form.get_user()
        if user.activation_date is None:
            today = datetime.date.today()
            user.activation_date = today
            if user.subscription_days:
                user.end_of_subscription = today + datetime.timedelta(days=user.subscription_days)
                user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


def add_stop_word(request):
    user = request.user
    StopWords(user=user, word=request.POST.get('word')).save()
    return HttpResponse("form is added")


def del_stop_word(request):
    user = request.user
    stop_word = request.POST.get('stop_word')
    stop_word = StopWords.objects.get(user=user, id=stop_word)
    stop_word.delete()
    return HttpResponse("stop_word was delited")


def add_change_refresh_interval(request):
    try:
        interval = RefreshInterval.objects.get(user=request.user)
    except:
        interval = None
    start = request.POST.get("start")
    end = request.POST.get("end")
    if interval is None:
        RefreshInterval(start=start, end=end, user=request.user).save()
    else:
        refresh_interval = RefreshInterval.objects.get(user=request.user)
        refresh_interval.start = start
        refresh_interval.end = end
        refresh_interval.save()
    return HttpResponse("Интервал сохранен")


def add_bitrix_data(request):
    try:
        data = BitrixAccountData.objects.get(user=request.user)
    except:
        data = None
    login = request.POST.get("login")
    password = request.POST.get("password")
    if data is None:
        BitrixAccountData(login=login, password=password, user=request.user).save()
    else:
        data.login = login
        data.password = password
        data.save()
    return HttpResponse("Данные для входа сохранены")
