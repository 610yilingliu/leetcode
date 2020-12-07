#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#

# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    
class CustomStack:

    def __init__(self, maxSize):
        self.ms = maxSize
        self.leng = 0
        self.top = None
        

    def push(self, x: int):
        if not self.top and self.ms > 0:
            self.top = Node(x)
            self.leng = 1
        elif self.leng < self.ms:
            cur = Node(x)
            cur.next = self.top
            self.top = cur
            self.leng += 1

    def pop(self):
        if self.leng == 0:
            return -1
        return_num = self.top.val
        self.top = self.top.next
        self.leng -= 1
        return return_num

    def increment(self, k, val):
        if self.leng < k:
            cur = self.top
            while cur:
                cur.val += val
                cur = cur.next
        else:
            curpos = 0
            cur = self.top
            while curpos < self.leng - k:
                cur = cur.next
                curpos += 1
            while cur:
                cur.val += val
                cur = cur.next
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(3)
# obj.push(1)
# obj.push(2)
# obj.pop()
# obj.push(2)
# obj.push(3)
# obj.push(4)
# obj.increment(5, 100)
# obj.increment(2, 100)
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# @lc code=end

