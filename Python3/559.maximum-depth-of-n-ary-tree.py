#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.children:
            return 1
        d = 1 + max(self.maxDepth(child) for child in root.children)
        return d





# @lc code=end

