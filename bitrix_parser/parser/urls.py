from django.urls import path
from .views import index, MyLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", index, name='index'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
