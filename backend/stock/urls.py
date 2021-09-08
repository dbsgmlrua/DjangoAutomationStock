from django.urls import path
from . import views
from .views import Starter, Checker, getStockList, getStockDetail, getStockOhlc, customExceptionHandler

urlpatterns = [
    path('test', views.thread, name='test-home'),
    path('starter', Starter),
    path('check', Checker),
    path('stocks', getStockList),
    path('exceptions', customExceptionHandler),
    path('stocks/<slug:code>', getStockDetail),
    path('stocks/<slug:code>/ohlc', getStockOhlc)
    
]