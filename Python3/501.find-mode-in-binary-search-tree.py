#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#
from collections import deque

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root):
        self.d = dict()
        mx_ls = []
        mxval = 0
        self.dfs(root)
        for key in self.d:
            if self.d[key] > mxval:
                mxval = self.d[key]
        for key in self.d:
            if self.d[key] == mxval:
                mx_ls.append(key)
        return mx_ls

    def dfs(self, root):
        if not root:
            return
        self.d[root.val] = self.d.get(root.val, 0) + 1
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)

def construct_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    leng = len(values)
    nums = 1
    while nums < leng:
             node = queue.popleft()
             if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1
    return root

if __name__ == '__main__':
    a = construct_tree([1,None,2,2])
    print(a)
# @lc code=end

