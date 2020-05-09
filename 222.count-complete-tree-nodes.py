#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode):
        if not root:
            return 0
        self.counter = 0
        self.traveller(root)
        return self.counter
    def traveller(self, root):
        if not root:
            return
        self.counter += 1
        self.traveller(root.left)
        self.traveller(root.right)
                
# @lc code=end
