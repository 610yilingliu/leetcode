#
# @lc app=leetcode id=1117 lang=python3
#
# [1117] Building H2O
#

# @lc code=start
import time
import random
from threading import Thread, Lock

class H2O:
    def __init__(self):
        self.h = 0
        self.o = 0
        self.h2o_thread = Thread(target=self.h2o, args=())
        self.h2o_thread.setDaemon(True)
        self.h2o_thread.start()
        self.h_lock = Lock()
        self.o_lock = Lock()
        self.hl = Lock()
        self.ol = Lock()
        pass

    def h2o(self):
        while True:
            if self.h >= 2 and self.o >= 1:
                # self.hl.acquire()
                self.h -= 2
                # self.hl.release()
                # self.ol.acquire()
                self.o -= 1
                # self.ol.release()
            time.sleep(0.01)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]'):
        self.h_lock.acquire()
        while self.h >= 2:
            time.sleep(0.01)
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        # self.hl.acquire()
        self.h += 1
        # self.hl.release()
        self.h_lock.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]'):
        self.o_lock.acquire()
        while self.o >= 1:
            time.sleep(0.01)
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        # self.ol.acquire()
        self.o += 1
        # self.ol.release()
        self.o_lock.release()
# @lc code=end

