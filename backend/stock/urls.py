from django.urls import path
from . import views
from .views import Checker, Starter

urlpatterns = [
    # path('', views.thread, name='test-home'),
    path('checker', Checker),
    path('starter', Starter)
]