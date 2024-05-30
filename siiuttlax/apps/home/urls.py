from django.urls import path
from django.urls import include

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
]