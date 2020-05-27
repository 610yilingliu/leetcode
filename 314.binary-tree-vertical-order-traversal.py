#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def verticalOrder(self, root: TreeNode):
        if not root:
            return []
        self.d = collections.defaultdict(list)
        self.traveller(root, 0)
        # minimun index number in the dict
        mi_k = float('inf')
        # maximun index number in the dict
        mx_k = float('-inf')
        for key in self.d:
            mi_k = min(key, mi_k)
            mx_k = max(key, mx_k)
        intercept = -mi_k
        # how many levels are there in the input tree?
        mx_k = mx_k + intercept
        ans = [None for _ in range(mx_k + 1)]
        for k, v in self.d.items():
            ans[k + intercept] = v
        return ans
    # level order traversal
    def traveller(self, root, level):
        if not root:
            return
        q = collections.deque([(root, level)])
        while q:
            curroot = q.popleft()
            self.d[curroot[1]].append(curroot[0].val)
            if curroot[0].left:
                q.append((curroot[0].left, curroot[1] - 1))
            if curroot[0].right:
                q.append((curroot[0].right, curroot[1] + 1))
        

# def construct_tree(values):
#     if not values:
#         return None
#     root = TreeNode(values[0])
#     queue = collections.deque([root])
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
    
# if __name__ == '__main__':
#     a = Solution()
#     tree = construct_tree([3,9,20,None,None,15,7])
#     b = a.verticalOrder(tree)
#     print(b)
# @lc code=end

