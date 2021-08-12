from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
from stock.classes.MainThread import MainThread, MainThread2
from multiprocessing import Process, Queue
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from stock.classes.CreaonChecker import CreonChecker, CreonStarter
from stock.classes.CreonBalance import CreonBalance

#Serializer
from stock.serializerObjects.HtsChecker import HtsChecker
from stock.serializerObjects.HtsStarter import HtsStarter
from rest_framework.response import Response
from stock.serializers import HtsCheckerSerializer, HtsStarterSerializer

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
    starter = CreonStarter()
    starter.start_creon_plus()
    ss = HtsStarter("Success!")
    serializer = HtsStarterSerializer(ss)
    return Response(serializer.data)

#주식리스트
@api_view(['GET'])
@permission_classes([AllowAny])
def geeStockList(request):
    return Response()

#주식디테일
@api_view(['GET'])
@permission_classes([AllowAny])
def geeStockDetail(request):
    return Response()

#구매하기
@api_view(['POST'])
@permission_classes([AllowAny])
def buyStock(request):
    return Response()

#팔기
@api_view(['POST'])
@permission_classes([AllowAny])
def sellStock(request):
    return Response()


### 테스트 api ###