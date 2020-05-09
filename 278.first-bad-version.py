#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

# @lc code=end

