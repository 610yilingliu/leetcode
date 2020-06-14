#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        if not root:
            return 0
        return self.pathSum(root.left,sum) + self.pathSum(root.right,sum) + self.adder(root, sum)
        

    def adder(self, root, rest):
        cur = 0
        if not root:
            return cur
        rest = rest - root.val
        if rest == 0:
            cur += 1
        cur += self.adder(root.left, rest)
        cur += self.adder(root.right, rest)
        return cur

# @lc code=end

