from django.urls import path
from . import views
from .views import Checker, Starter, StockList, StockDetail

urlpatterns = [
    # path('', views.thread, name='test-home'),
    path('checker', Checker),
    path('starter', Starter),
    path('stocks', StockList),
    path('stocks/<slug:code>', StockDetail)
]