#
# @lc app=leetcode id=364 lang=python3
#
# [364] Nested List Weight Sum II
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
import collections
class Solution:
    def depthSumInverse(self, nestedList):
        if not nestedList:
            return 0
        start = 0
        self.distr = collections.defaultdict(list)
        self.getnums(nestedList, start)
        keys = [k for k in self.distr]
        if keys:
            deepest = max(keys)
        else:
            return 0
        ans = 0
        for k, v in self.distr.items():
            ans += ((deepest - k) + 1) * sum(v)
        return ans
    
    def getnums(self, nestedList, curlevel):
        if nestedList != []:
            for item in nestedList:
                integer = item.getInteger()
                if integer is not None:
                    self.distr[curlevel].append(integer)
                else:
                    self.getnums(item.getList(), curlevel + 1)

# @lc code=end

