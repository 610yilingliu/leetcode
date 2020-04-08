#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        if root is not None:
            ls = []
            counter = 0
            def router(root, counter):
                counter += 1
                if len(ls) < counter:
                    ls.append([])
                ls[counter - 1].append(root.val)
                if root.left is not None:
                    router(root.left, counter)
                if root.right is not None:
                    router(root.right, counter)
            router(root, counter)
            ans = [sum(cell)/len(cell) for cell in ls]
            return ans
        return []


# @lc code=end

