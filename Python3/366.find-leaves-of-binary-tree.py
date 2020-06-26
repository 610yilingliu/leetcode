#
# @lc app=leetcode id=366 lang=python3
#
# [366] Find Leaves of Binary Tree
#
import collections
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: 'TreeNode') -> 'List[List[int]]':
        def getLevel(root, d):
            if not root:
                return 0
            left = getLevel(root.left, d)
            right = getLevel(root.right, d)
            level = 1 + max(left, right)
            d[level].append(root.val)
            return level
        
        d = collections.defaultdict(list)
        getLevel(root, d)
        res = []
        for k in sorted(d.keys()):
            res.append(d[k])
        return res


# @lc code=end

