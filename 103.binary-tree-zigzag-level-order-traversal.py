#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

# class Solution:
#     def zigzagLevelOrder(self, root):
#         if not root:
#             return []
#         ans = []
#         level = 0
#         def traveller(root, level):
#             if len(ans) <= level:
#                 ans.append([])
#             # equal to if level//2 == 1, level is the index of current row
#             if level & 1:
#                 ans[level].insert(0, root.val)             
#             else:
#                 ans[level].append(root.val)
#             if root.left:
#                 traveller(root.left, level + 1)
#             if root.right:
#                 traveller(root.right, level + 1)
#         traveller(root, level)
#         return ans

class Solution:
    def zigzagLevelOrder(self, root):
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
        if len(ans) > 1:
            for item in ans[1::2]:
                item.reverse()
        return ans

if __name__ == '__main__':
    a = construct_tree([3,9,20,None,None,15,7])
    b = Solution()
    c = b.zigzagLevelOrder(a)
    print(c)
            
# @lc code=end

