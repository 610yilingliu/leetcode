#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.pre = None
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.first:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.inorder(root.right)
            
        
        


# @lc code=end

