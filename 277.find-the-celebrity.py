#
# @lc app=leetcode id=277 lang=python3
#
# [277] Find the Celebrity
#

# @lc code=start
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        # Find the candidate.
        for i in range(1, n):
            if knows(candidate, i):  # All candidates < i are not celebrity candidates.
                candidate = i
        # Verify the candidate.
        for i in range(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        return candidate
            
            


# @lc code=end

