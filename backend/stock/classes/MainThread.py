from stock.classes.core.MThread import MThread
from threading import Thread
import time

class MainThread(MThread):
    def InfiniteLoop(self):
        while True:
            print("working1")
            time.sleep(1)

class MainThread2(MThread):
    def InfiniteLoop(self):
        while True:
            print("working2")
            time.sleep(1)