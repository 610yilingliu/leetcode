#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root, k):
        if not root:
            return False
        visited = set()
        def finder(root):
            if not root:
                return False
            if k - root.val in visited:
                return True
            visited.add(root.val)
            return finder(root.left) or finder(root.right)
        return finder(root)


            
# @lc code=end

