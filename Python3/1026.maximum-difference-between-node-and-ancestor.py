#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.s = 0
        
        def find(node, path):
            if not node:                
                return 
 
            tmp = max(abs(max(path) - node.val), abs(min(path) - node.val))
            self.s = max(self.s, tmp)
            
            path.append(node.val)
            
            find(node.left, path)
            find(node.right, path)
            path.pop()
            
        find(root, [root.val])
        return self.s

# @lc code=end

