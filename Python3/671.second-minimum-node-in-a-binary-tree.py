#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque

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

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        self.base = root.val
        self.ans = float('inf')
        self.finder(root)
        if self.ans != float('inf'):
            return self.ans
        return -1
    def finder(self, root):
        if not root:
            return
        if self.base < root.val < self.ans:
            self.ans = root.val
        if root.left:
            self.finder(root.left)
        if root.right:
            self.finder(root.right)

if __name__ == '__main__':
    tree = construct_tree([2,2,5,None,None,5,7])
    b = Solution()
    c = b.findSecondMinimumValue(tree)
    print(c)
# @lc code=end

