#
# @lc app=leetcode id=346 lang=python3
#
# [346] Moving Average from Data Stream
#
import collections
# @lc code=start
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.cur = collections.deque()
        self.num = 0
        self.size = size
        

    def next(self, val: int) -> float:
        if len(self.cur) == self.size:
            self.cur.popleft()
        self.cur.append(val)
        if self.num < self.size:
            self.num += 1
        return sum(self.cur)/self.num


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# @lc code=end

