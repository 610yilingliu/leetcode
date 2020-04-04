#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

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

def ls_to_tree(ls, cur = 0):
    if not ls:
        return None
    root = TreeNode(ls[cur])
    next_left = ((cur + 1) << 1) - 1
    next_right = (cur + 1) << 1
    if next_left < len(ls):
        if ls[next_left] is not None:
            root.left = ls_to_tree(ls, next_left)
    if next_right < len(ls):  
        if ls[next_right] is not None:
            root.right = ls_to_tree(ls, next_right)
    return root


if __name__ == '__main__':
    a = ls_to_tree([1,1,2,2,3,4,5])
    b = Solution()
    c = b.findMode(a)
    print(c)
# @lc code=end

