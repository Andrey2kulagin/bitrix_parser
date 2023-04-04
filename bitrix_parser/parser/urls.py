from django.urls import path
from .views import parsing, index

urlpatterns = [
    path("", index, name='index'),
    path("parsing", parsing, name='parsing')
]
