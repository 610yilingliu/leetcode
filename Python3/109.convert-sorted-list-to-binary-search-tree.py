#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        # put values in listnode into a list
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        # def tree_generator(ls):
        #     root_idx = len(ls) >> 1
        #     root = TreeNode(ls[root_idx])
        #     if ls[:root_idx]:
        #         root.left = tree_generator(ls[:root_idx])
        #     if ls[root_idx + 1:]:
        #         root.right = tree_generator(ls[root_idx + 1:])
        #     return root
        # return tree_generator(ls)
        def tree_generator(start, end):
            root_idx = start + ((end - start) >> 1)
            root = TreeNode(ls[root_idx])
            if start < root_idx:
                root.left = tree_generator(start, root_idx)
            if root_idx + 1 < end:
                root.right = tree_generator(root_idx + 1, end)
            return root
        return tree_generator(0, len(ls))
        
        
# @lc code=end

