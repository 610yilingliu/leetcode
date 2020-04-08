#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root):
        ls = []
        def generator(root):
            if not root:
                return
            for child in root.children:
                generator(child)
            ls.append(root.val)
        generator(root)
        return ls

# @lc code=end

