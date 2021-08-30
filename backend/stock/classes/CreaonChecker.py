import os, sys, ctypes
import win32com.client
import os
import time
import json
from django.core.exceptions import ImproperlyConfigured
from pywinauto import application

# 크레온 플러스 공통 OBJECT
cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode')
cpStatus = win32com.client.Dispatch('CpUtil.CpCybos')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
cpStock = win32com.client.Dispatch('DsCbo1.StockMst')
cpOhlc = win32com.client.Dispatch('CpSysDib.StockChart')
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033')
cpCash = win32com.client.Dispatch('CpTrade.CpTdNew5331A')
cpOrder = win32com.client.Dispatch('CpTrade.CpTd0311')  

with open(os.path.join(os.path.dirname(__file__), "secrets.json"), 'r') as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

# class CreonChecker():
#     def check_creon_system(self):
#         """크레온 플러스 시스템 연결 상태를 점검한다."""
#         # 관리자 권한으로 프로세스 실행 여부
#         if not ctypes.windll.shell32.IsUserAnAdmin():
#             print('check_creon_system() : admin user -> FAILED')
#             return False
    
#         # 연결 여부 체크
#         if (cpStatus.IsConnect == 0):
#             print('check_creon_system() : connect to server -> FAILED')
#             return False
    
#         # 주문 관련 초기화 - 계좌 관련 코드가 있을 때만 사용
#         if (cpTradeUtil.TradeInit(0) != 0):
#             print('check_creon_system() : init trade -> FAILED')
#             return False
#         return True

class CreonChecker():
    def check_creon_system(self):
        """크레온 플러스 시스템 연결 상태를 점검한다."""
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print('check_creon_system() : admin user -> FAILED')
            return False
    
        # 연결 여부 체크
        if (cpStatus.IsConnect == 0):
            print('check_creon_system() : connect to server -> FAILED')
            return False
    
        # 주문 관련 초기화 - 계좌 관련 코드가 있을 때만 사용
        if (cpTradeUtil.TradeInit(0) != 0):
            print('check_creon_system() : init trade -> FAILED')
            return False
        return True

class CreonStarter():
    def start_creon_plus(self):       
        os.system('taskkill /IM coStarter* /F /T')
        os.system('taskkill /IM CpStart* /F /T')
        os.system('wmic process where "name like \'%coStarter%\'" call terminate')
        os.system('wmic process where "name like \'%CpStart%\'" call terminate')
        time.sleep(5)        

        app = application.Application()
        app.start("C:\CREON\STARTER\coStarter.exe /prj:cp /id:{fId} /pwd:{fPwd} /pwdcert:{fPwdCert} /autostart".format(fId=get_secret("ID"), fPwd=get_secret("PW"), fPwdCert=get_secret("PWDCERT")))