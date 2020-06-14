#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.q:
            res = self.q[0]
            self.q = self.q[1:]
            return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.q:
            return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.q:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

