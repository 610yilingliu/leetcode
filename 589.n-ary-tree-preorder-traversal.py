#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root):
        ls = []
        def traveller(root):
            if not root:
                return
            ls.append(root.val)
            for child in root.children:
                traveller(child)
        traveller(root)
        return ls



# @lc code=end

