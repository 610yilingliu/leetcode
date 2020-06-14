#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.compare(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


    def compare(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.compare(s.right, t.right) and self.compare(s.left, t.left)



# @lc code=end

