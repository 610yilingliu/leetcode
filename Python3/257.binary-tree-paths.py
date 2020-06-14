#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return[]
        self.ans = []
        self.generator(root, str(root.val))
        return self.ans

    def generator(self, root, string):
        if root.left is None and root.right is None:
            self.ans.append(string)
        if root.left:
            self.generator(root.left, string + '->' + str(root.left.val))
        if root.right:
            self.generator(root.right, string + '->' + str(root.right.val))


# @lc code=end

