#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        self.mxs = []
        self.generator(root, 0)
        return self.mxs
        
    def generator(self, root, curlevel):
        if not root:
            return
        if curlevel >= len(self.mxs):
            self.mxs.append(root.val)
        else:
            self.mxs[curlevel] = max(self.mxs[curlevel], root.val)
        self.generator(root.left, curlevel + 1)
        self.generator(root.right, curlevel + 1)
# @lc code=end

