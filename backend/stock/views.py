from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
from stock.classes.MainThread import MainThread, MainThread2
from multiprocessing import Process, Queue
from rest_framework.decorators import api_view, permission_classes
from stock.classes.CreaonChecker import CreonChecker
from stock.classes.CreonBalance import CreonBalance

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
        stocks = checker.get_stock_balance()
        return JsonResponse({
            'stocks': stocks
        })


class Stock(View):
    def get(self, request, code):
        checker = CreonBalance()
        stock_name, bought_qty = checker.get_stock_info(code)
        return JsonResponse({
            'stock_name': stock_name,
            'bought_qty': bought_qty
        })

class GetOhlc(View):
    def get(self, request, code, qty):
        checker = CreonBalance()
        ohlc = checker.get_ohlc(code, qty).to_json(orient='records')
        print(ohlc)
        return JsonResponse(json.loads(ohlc), safe=False)
