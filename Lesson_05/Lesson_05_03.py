import threading
from threading import Thread
import random
import time

class RandomGeneratorThread(threading.Thread):

    def __init__(self, num, name):
        self._num = num
        self._name = name
        Thread.__init__( self, name=self._name )

    def run(self):
        for i in range(self._num):
            time.sleep(random.randint(0, 5))
            print( f"I'm executing from {self._name}" )
        print( f"the end of {self._name}")

a = RandomGeneratorThread(10, "Thread a")
b = RandomGeneratorThread(10, "Thread b")
a.daemon = True
b.daemon = True
a.start()
b.start()