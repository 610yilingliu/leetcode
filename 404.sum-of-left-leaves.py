#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        if not root or (not root.left and not root.right):
            return 0
        self.ans = 0
        self.generator(root, True)
        return self.ans


    def generator(self, root, sign = False):
        if root.left is None and root.right is None:
            if sign == True:
                self.ans += root.val
                return
        if root.left:
            self.generator(root.left, sign = True)
        if root.right:
            self.generator(root.right, sign = False)
        

# @lc code=end

