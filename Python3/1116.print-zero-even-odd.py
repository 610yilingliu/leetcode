#
# @lc app=leetcode id=1116 lang=python3
#
# [1116] Print Zero Even Odd
#

# @lc code=start
from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zerolock = Lock()
        self.oddlock = Lock()
        self.evenlock = Lock()
        self.oddlock.acquire()
        self.evenlock.acquire()
                
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]'):
        for i in range(1, self.n + 1):
            self.zerolock.acquire()
            printNumber(0)
            if(i & 1):
                try:
                    self.oddlock.release()
                except:
                    continue
            else:
                try:
                    self.evenlock.release()
                except:
                    continue              
        
    def even(self, printNumber: 'Callable[[int], None]'):
        for i in range(2, self.n + 1, 2):
            self.evenlock.acquire()
            printNumber(i)
            try:
                self.zerolock.release()
            except:
                continue
            
    def odd(self, printNumber: 'Callable[[int], None]'):
        for i in range(1, self.n + 1, 2):
            self.oddlock.acquire()
            printNumber(i)
            try:
                self.zerolock.release()
            except:
                continue
        
# @lc code=end

