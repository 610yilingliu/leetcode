#
# @lc app=leetcode id=742 lang=python3
#
# [742] Closest Leaf in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# import collections

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def findClosestLeaf(self, root, k):
#         self.parent_dic = dict()
#         self.target = None
#         self.dict_generator(root, k)
#         self.shortest = float('inf')
#         self.ans = None
#         self.dist_finder(self.target, 0)
#         back_step = 1
#         start = self.target
#         while start in self.parent_dic and back_step + 1 < self.shortest:
#             start = self.parent_dic[start]
#             self.dist_finder(start, back_step)
#             back_step += 1
#         return self.ans

#     def dict_generator(self, root, destination):
#         if not root:
#             return
#         if root.val == destination:
#             self.target = root
#         if root.left:
#             self.parent_dic[root.left] = root
#         if root.right:
#             self.parent_dic[root.right] = root
#         self.dict_generator(root.left, destination)
#         self.dict_generator(root.right, destination)
        
#     def dist_finder(self, node, curdist):
#         if not node.left and not node.right:
#             if self.shortest > curdist + 1:
#                 self.ans = node.val
#             return
#         if node.left:
#             self.dist_finder(node.left, curdist + 1)
#         if node.right:
#             self.dist_finder(node.right, curdist + 1)
            
# def tree_builder(values):
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
#     tree = tree_builder([1,2,3,4, None, None, None, 5, None,6])
#     b = a.findClosestLeaf(tree, 2)
#     print(b)

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        parents = {}
        leaves = []
        self.knode = None
        def traverse(root):
            if root.val == k: self.knode = root
            if not root.left and not root.right:
                leaves.append(root)
                return
            for child in (root.left, root.right):
                if not child: continue
                traverse(child)
                parents[child.val] = root
        def findParents(node):
            ans = [node.val]
            while node.val in parents:
                node = parents[node.val]
                ans.append(node.val)
            return ans
        traverse(root)
        kParents = findParents(self.knode)
        ans, dist = None, 0x7FFFFFFF
        for leaf in leaves:
            leafParents = findParents(leaf)
            cross = [n for n in leafParents if n in kParents][0]
            ndist = leafParents.index(cross) + kParents.index(cross)
            if ndist < dist:
                dist = ndist
                ans = leaf
        return ans.val
# @lc code=end

