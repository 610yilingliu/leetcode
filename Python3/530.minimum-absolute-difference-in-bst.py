#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root):
        minimum = float('inf')
        ls = self.inorder(root, [])
        for i in range(1, len(ls)):
            minimum = min(ls[i] - ls[i - 1], minimum)
        return minimum

    def inorder(self, root, temp):
        if root == None:
            return
        self.inorder(root.left, temp)
        temp.append(root.val)
        self.inorder(root.right, temp)
        return temp

# @lc code=end

