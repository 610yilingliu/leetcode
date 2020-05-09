#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        storage = []
    
        def traveller(root, level):
            if len(storage) <= level:
                storage.append([])
            storage[level].append(root.val)
            if root.left:
                traveller(root.left, level + 1)
            if root.right:
                traveller(root.right, level + 1)

        traveller(root, 0)
        ans = []
        for level in storage:
            ans.append(level[-1])
        return ans

# @lc code=end

