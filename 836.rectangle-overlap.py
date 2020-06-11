#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#

# @lc code=start
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        [A, B, C, D], [E, F, G, H] = rec1, rec2
        x, y = (min(C, G) - max(A, E)), (min(D, H) - max(B, F))
        return x > 0 and y > 0
# @lc code=end

