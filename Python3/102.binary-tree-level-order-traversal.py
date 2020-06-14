#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        ans = []
        level = 0
        def traveller(root, level):
            if len(ans) <= level:
                ans.append([])
            ans[level].append(root.val)
            if root.left:
                traveller(root.left, level + 1)
            if root.right:
                traveller(root.right, level + 1)
        traveller(root, level)
        return ans
# @lc code=end

