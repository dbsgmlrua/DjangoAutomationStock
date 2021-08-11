from stock.classes.core.MThread import MThread
from threading import Thread
import time
from stock.classes.MyBalance import MyBalance

class MainThread(MThread):
    def InfiniteLoop(self):
        # t1 = MyBalance()
        # t1.setName("T1")
        # t2 = MyBalance()
        # t2.setName("T2")
        i = 0
        while True:
            # t1.getName()
            # t2.getName()  
            print(i)
            i += 1
            time.sleep(1)

class MainThread2(MThread):
    def InfiniteLoop(self):
        i = 0
        while True:  
            print(i)
            i += 1        
            time.sleep(1)