#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        if n < 1:
            return []
        return self.generator(1, n)

    def generator(self, l, r):
        if l > r:
            return [None]
        if l == r:
            return [TreeNode(l)]
        res = []
        for i in range(l, r + 1):
            left = self.generator(l, i - 1)
            right = self.generator(i + 1, r)
            for m in left:
                for n in right:
                    node = TreeNode(i)
                    node.left = m
                    node.right = n
                    res.append(node)
        return res

if __name__ == '__main__':
    a = Solution()
    b = a.generateTrees(3)
    print(b)

# @lc code=end

