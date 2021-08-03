from threading import Thread
import time
from stock.classes.core.Singleton import Singleton

class MThread:
    NotLoop = True
    
    def startLoop(self):
        if self.NotLoop:
            print("startWorking")
            self.NotLoop = False
            self.InfiniteLoop()

    def InfiniteLoop(self):
        return False