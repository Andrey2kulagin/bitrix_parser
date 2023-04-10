import django.forms as forms
from .models import RefreshInterval, StopWords, BitrixAccountData


class RefreshIntervalForm(forms.ModelForm):
    start = forms.CharField(max_length=200, label="От (сек.)",
                            widget=forms.NumberInput(
                                attrs={"class": "name_input", "type": "number", "min": 1}))
    end = forms.CharField(max_length=200, label="До (сек.)",
                          widget=forms.NumberInput(
                              attrs={"class": "name_input", "type": "number", "min": 1}))

    class Meta:
        model = RefreshInterval
        fields = [
            "start",
            "end"
        ]


class StopWordsForm(forms.ModelForm):
    word = forms.CharField(label="",
                           widget=forms.TextInput(attrs={"class": "login_input username_input",
                                                         "placeholder": "Введите стоп-слово"}))

    class Meta:
        model = StopWords
        fields = [
            "word",
        ]


class BitrixAccountDataForm(forms.ModelForm):
    login = forms.CharField(label="",
                            widget=forms.TextInput(attrs={"class": "login_input username_input",
                                                          "placeholder": "Введите логин от Bitrix"}))
    password = forms.CharField(label="",
                               widget=forms.TextInput(attrs={"class": "login_input username_input",
                                                             "placeholder": "Введите пароль от Bitrix"}))

    class Meta:
        model = BitrixAccountData
        fields = [
            "login",
            "password"
        ]
