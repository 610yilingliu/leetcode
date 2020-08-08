#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#
# https://leetcode.com/problems/valid-square/description/
#
# algorithms
# Medium (42.29%)
# Likes:    246
# Dislikes: 421
# Total Accepted:    35.4K
# Total Submissions: 82.2K
# Testcase Example:  '[0,0]\n[1,1]\n[1,0]\n[0,1]'
#
# Given the coordinates of four points in 2D space, return whether the four
# points could construct a square.
# 
# The coordinate (x,y) of a point is represented by an integer array with two
# integers.
# 
# Example:
# 
# 
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
# 
# 
# 
# 
# Note:
# 
# 
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal
# angles (90-degree angles).
# Input points have no order.
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def d(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
        s = set([d(p1, p2), d(p1, p3), d(p1, p4), d(p2, p3), d(p2, p4), d(p3, p4)])
        return 0 not in s and len(s) == 2
# @lc code=end

