#
# @lc app=leetcode id=379 lang=python3
#
# [379] Design Phone Directory
#

# @lc code=start
class linkedlist:
    def __init__(self, val):
        self.val = val
        self.next = None

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        if maxNumbers > 0:
            self.current = linkedlist(0)
            self.head = linkedlist(-1)
            self.head.next = self.current
            for i in range(1, maxNumbers):
                self.current.next = linkedlist(i)
                self.current = self.current.next
        self.available = {num for num in range(maxNumbers)}
        

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.head.next is not None:
            tmp = self.head.next
            if self.head.next.next is not None:
                self.head.next = self.head.next.next
            else:
                self.head.next = None
            val = tmp.val
            self.available.remove(val)
            return val
        return self.head.val

    def check(self, number: int):
        """
        Check if a number is available or not.
        """
        if number in self.available:
            return True
        return False
        

    def release(self, number: int):
        """
        Recycle or release a number.
        """
        if number not in self.available:
            a = None
            if self.head.next is not None:
                a = self.head.next
            self.head.next = linkedlist(number)
            self.head.next.next = a
            self.available.add(number)
            
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
# @lc code=end

