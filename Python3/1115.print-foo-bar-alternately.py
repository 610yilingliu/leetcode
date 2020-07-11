#
# @lc app=leetcode id=1115 lang=python3
#
# [1115] Print FooBar Alternately
#

# @lc code=start
from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.fool = Lock()
        self.barl = Lock()
        self.barl.acquire()


    def foo(self, printFoo: 'Callable[[], None]'):
        
        for i in range(self.n):
            
            # printFoo() outputs "foo". Do not change or remove this line.
            self.fool.acquire()
            printFoo()
            self.barl.release()


    def bar(self, printBar: 'Callable[[], None]'):
        
        for i in range(self.n):
            
            # printBar() outputs "bar". Do not change or remove this line.
            self.barl.acquire()
            printBar()
            self.fool.release()
# @lc code=end

