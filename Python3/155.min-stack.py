#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int):
        self.stack.append(x)
        if len(self.minstack) == 0 or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self):
        top = self.stack[-1]
        self.stack.pop()
        if top == self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

