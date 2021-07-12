from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from stock.classes.MainThread import MainThread, MainThread2
from multiprocessing import Process, Queue
from rest_framework.decorators import api_view, permission_classes
from stock.classes.CreaonChecker import CreonChecker
from stock.classes.CreonBalance import CreonBalance


from .serializers import RunningCheckerSerializer

def thread(request):
    a = MainThread()
    b = MainThread2()
    
    th1 = Process(target=a.startLoop)
    th2 = Process(target=b.startLoop)

    th1.start()
    th2.start()
    return render(request, 'tester/home.html')

class Checker(View):
    def get(self, request):
        checker = CreonChecker()
        return JsonResponse({
            'running': checker.check_creon_system()
        })

class Starter(View):
    def get(self, request):
        checker = CreonChecker()
        checker.start_creon_plus()
        return JsonResponse({
            'start': 'Success!'
        })

class Balance(View):
    def get(self, request):
        checker = CreonBalance()
        stocks = checker.get_stock_balance('ALL')
        return JsonResponse({
            'stock_name': 'Success!'
        })


class Stock(View):
    def get(self, request, code):
        checker = CreonBalance()
        stock_name, bought_qty = checker.get_stock_balance(code)
        return JsonResponse({
            'stock_name': stock_name,
            'bought_qty': bought_qty
        })
