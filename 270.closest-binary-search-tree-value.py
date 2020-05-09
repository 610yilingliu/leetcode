#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root is None:
            return float('inf')

        if root.val == target:
            return root.val
        elif root.val < target:
            rightRes = self.closestValue(root.right, target)
            return root.val if abs(root.val - target) < abs(rightRes - target) else rightRes
        elif root.val > target:
            leftRes = self.closestValue(root.left, target)
            return root.val if abs(root.val - target) < abs(leftRes - target) else leftRes
        
        
            


# @lc code=end

