from django.urls import path
from . import views
from .views import Starter, Checker

urlpatterns = [
    path('test', views.thread, name='test-home'),
    path('starter', Starter),
    path('check', Checker)
]