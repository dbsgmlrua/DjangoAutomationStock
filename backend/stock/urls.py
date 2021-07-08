from django.urls import path
from . import views
from .views import Checker, Starter, Balance, Stock

urlpatterns = [
    path('', views.thread, name='test-home'),
    path('checker', Checker.as_view(), name='checker'),
    path('starter', Starter.as_view(), name='starter'),
    path('balance', Balance.as_view(), name='balance'),
    path('stocks/<slug:code>', Stock.as_view(), name='stockinfo')
]