from django.urls import path
from . import views
from .views import Checker, Starter, Balance

urlpatterns = [
    path('', views.thread, name='test-home'),
    path('checker', Checker.as_view(), name='checker'),
    path('starter', Starter.as_view(), name='starter'),
    path('balance/<slug:code>', Balance.as_view(), name='balance')
]