#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#
import collections
# @lc code=start
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []

    def addNum(self, val):
        if len(self.s) < 2:
            self.s.append(val)
            self.s.append(val)
        if val in self.s:
            return
        else:
            idx = self.binarysearch(val)
            if idx & 1:
                
        
    def binarysearch(self, target):
        l = 0
        r = len(self.s) - 1
        while l < r:
            mid = (l + r) >> 1
            if self.s[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l
                

    def getIntervals(self) -> List[List[int]]:
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# @lc code=end

