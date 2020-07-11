#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#

# @lc code=start

from threading import Lock

class Foo:
    def __init__(self):
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock1.acquire()
        self.lock2.acquire()



    def first(self, printFirst: 'Callable[[], None]'):
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()


    def second(self, printSecond: 'Callable[[], None]'):
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.lock1:
            printSecond()
            self.lock2.release()


    def third(self, printThird: 'Callable[[], None]'):
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.lock2:
            printThird()
# @lc code=end

