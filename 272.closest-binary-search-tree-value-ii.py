#
# @lc app=leetcode id=272 lang=python3
#
# [272] Closest Binary Search Tree Value II
#

# @lc code=start
# Definition for a binary tree node.
# from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def construct_tree(values):
#     if not values:
#         return None
#     root = TreeNode(values[0])
#     queue = deque([root])
#     leng = len(values)
#     nums = 1
#     while nums < leng:
#              node = queue.popleft()
#              if node:
#                 node.left = TreeNode(values[nums]) if values[nums] else None
#                 queue.append(node.left)
#                 if nums + 1 < leng:
#                     node.right = TreeNode(values[nums+1]) if values[nums+1] else None
#                     queue.append(node.right)
#                     nums += 1
#                 nums += 1
#     return root

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int):
        if not root:
            return []
        self.ls = []
        self.inorder(root)
        if target <= self.ls[0]:
            return self.ls[:k]
        if target >= self.ls[-1]:
            return self.ls[-k:]
        for i in range(len(self.ls) - 1):
            if self.ls[i] < target and self.ls[i + 1] >= target:
                left = i
                right = i + 1
                break
        ans = []
        count = 0
        while count < k:
            if left is not None and right is not None:
                if abs(self.ls[left] - target) <= abs(self.ls[right] - target):
                    ans.append(self.ls[left])
                    left -= 1
                    if left < 0:
                        left = None
                else:
                    ans.append(self.ls[right])
                    right += 1
                    if right >= len(self.ls):
                        right = None
            elif left is None:
                ans.append(self.ls[right])
                right += 1
            elif right is None:
                ans.append(self.ls[left])
                left -= 1
            count += 1
        return ans


    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.ls.append(root.val)
        self.inorder(root.right)

# if __name__ == '__main__':
#     tree = construct_tree([8, 1])
#     a = Solution()
#     b = a.closestKValues(tree, 6.0, 1)
#     print(b)
# @lc code=end

