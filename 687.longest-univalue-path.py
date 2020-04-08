#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#

# @lc code=start
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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        if not root:
            return 0
        self.mx = 0
        self.finder(root)
        return self.mx

    def finder(self,root):
        if not root:
            return 0
        left = self.finder(root.left)
        right = self.finder(root.right)
        l = 0
        r = 0
        # do not use left += 1
        if root.left and root.left.val == root.val:
            l = left + 1
        if root.right and root.right.val == root.val:
            r = right + 1
        self.mx = max(self.mx, l + r)
        return max(l, r)
        

if __name__ == '__main__':
    tree = construct_tree([5,4,5,1,1,5])
    b = Solution()
    c = b.longestUnivaluePath(tree)
    print(c)
# @lc code=end

