#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode):
        if not root:
            return 0
        self.bins = []
        self.finder(root, '')
        ans = 0
        for item in self.bins:
            cur = 0
            digit = 0
            while item:
                cur += (int(item[-1]) & 1) * (1 << digit)
                item = item[:-1]
                digit += 1
            ans += cur
        return ans

    def finder(self, root, path):
        path = path + str(root.val)
        if not root.left and not root.right:
            self.bins.append(path)
            return
        if root.left:
            self.finder(root.left, path)
        if root.right:
            self.finder(root.right, path)

# @lc code=end

