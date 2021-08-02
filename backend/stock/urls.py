from django.urls import path
from . import views
from .views import Starter, Balance, BalanceStock, Stock, GetOhlc, Checker

urlpatterns = [
    path('', views.thread, name='test-home'),
    path('checker', Checker),
    path('starter', Starter),
    path('balance', Balance.as_view(), name='balance'),
    path('balancestocks', BalanceStock.as_view(), name='balancestocks'),
    path('stocks/<slug:code>', Stock.as_view(), name='stockinfo'),
    path('ohlc/<slug:code>/<int:qty>', GetOhlc.as_view(), name='ohlcinfo')
]