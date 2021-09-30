from django.urls import path
from . import views
from .views import Checker, Starter, StockList, StockDetail, StockDetailOhlc, GetBalance, customExceptionHandler

urlpatterns = [
    # path('', views.thread, name='test-home'),
    path('checker', Checker),
    path('starter', Starter),
    path('stocks', StockList),
    path('stocks/<slug:code>', StockDetail),
    path('stocks/<slug:code>/ohlc', StockDetailOhlc),
    path('balance', GetBalance),
    path('exceptions', customExceptionHandler)
]