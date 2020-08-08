#
# @lc app=leetcode id=426 lang=python3
#
# [426] Convert Binary Search Tree to Sorted Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node'):
        if not root:
            return
        self.vals = []
        self.travel_tree(root)
        head = Node(0)
        prenode = head
        for val in self.vals:
            curnode = Node(val)
            curnode.left = prenode
            if prenode:
                prenode.right = curnode
            prenode = curnode
        prenode.right = head.right
        head.right.left = prenode
        return head.right
        
    def travel_tree(self, node):
        if not node:
            return
        self.travel_tree(node.left)
        self.vals.append(node.val)
        self.travel_tree(node.right)
# @lc code=end

