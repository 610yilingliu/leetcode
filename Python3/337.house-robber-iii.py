#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.d = dict()
        return self.helper(root, False)
    
    def helper(self, root, parentUsed):
        if not root: return 0
        if (root, parentUsed) in self.d:
            return self.d[(root, parentUsed)]
        res = 0
        if parentUsed:
            res = self.helper(root.left, False) + self.helper(root.right, False)
        else:
            res = max(root.val + self.helper(root.left, True) + self.helper(root.right, True), self.helper(root.left, False) + self.helper(root.right, False))
        self.d[(root, parentUsed)] = res
        return res
# @lc code=end

