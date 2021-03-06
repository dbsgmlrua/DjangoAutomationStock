from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from stock.classes.MainThread import MainThread, MainThread2
from multiprocessing import Process, Queue
from rest_framework.decorators import api_view, permission_classes
#stock.classes
from stock.classes.CreonChecker import CreonChecker
from stock.classes.CreonStockDetail import CreonStockDetail
from stock.classes.CreonBalance import CreonBalance
from stock.classes.exceptions.StockExceptionHandler import CustomApiException, ErrorCode

#rest_frameworks
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import exception_handler

#serizlizers
from stock.serializerObjects.HtsChecker import HtsChecker
from stock.serializerObjects.HtsStarter import HtsStarter
from stock.serializers import HtsCheckerSerializer, HtsStarterSerializer, StockListSerializer, StockDetailSerializer, StockDetailOhlcSerializer, MyBalanceSerializer

#TestCode
from stock.classes.test.TestCodeDummy import ExceptionTestChecker

def thread(request):
    a = MainThread()
    b = MainThread2()
    
    th1 = Process(target=a.startLoop)
    th2 = Process(target=b.startLoop)

    th1.start()
    th2.start()

    return render(request, 'tester/home.html')

@api_view(['GET'])
@permission_classes([AllowAny])
def Checker(request):
    checker = CreonChecker()
    checker = HtsChecker(checker.check_creon_system())
    serializer = HtsCheckerSerializer(checker)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def Starter(request):
    starter = CreonChecker()
    starter.start_creon_plus()
    ss = HtsStarter("Success!")
    serializer = HtsStarterSerializer(ss)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def StockList(request):
    stocklist = CreonStockDetail()
    serializer = StockListSerializer(stocklist.get_stock_list(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def StockDetail(request, code):
    StockDetail = CreonStockDetail()
    serializer = StockDetailSerializer(StockDetail.get_stock_detail(code))
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def StockDetailOhlc(request, code):
    StockDetail = CreonStockDetail()
    serializer = StockDetailOhlcSerializer(StockDetail.get_stock_detail_ohlc(code), many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def GetBalance(request):
    StockBalance = CreonBalance()
    serializer = MyBalanceSerializer(StockBalance.get_balance())
    return Response(serializer.data)


#exception
@api_view(['GET'])
@permission_classes([AllowAny])
def customExceptionHandler(request):
    ExceptionTestChecker("cpzm")
    raise CustomApiException(500, "dmdel")