#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
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
    def subtreeWithAllDeepest(self, root: TreeNode):
        if not root:
            return None
        self.parent_dic = dict()
        self.depth = collections.defaultdict(list)
        self.depth[0] = root
        self.mxdepth = 0
        self.travel(root, 0)
        self.related_nodes = []
        self.walked = set()
        for node in self.depth[self.mxdepth]:
            self.searcher(node)
        mi = float('inf')
        ans = None
        for node in self.related_nodes:
            if node.val < mi:
                ans = node
                mi = node
        return ans
        

    def travel(self, root, depth):
        if not root.left and not root.right:
            return
        if root.left:
            self.parent_dic[root.left] = root
            self.depth[depth].append(root.left)
            self.mxdepth = max(self.mxdepth, depth)
            self.travel(root.left, depth + 1)
        if root.right:
            self.parent_dic[root.right] = root
            self.depth[depth].append(root.right)
            self.mxdepth = max(self.mxdepth, depth)
            self.travel(root.right, depth + 1)

    def searcher(self, curnode):
        while curnode in self.parent_dic and curnode not in self.walked:
            self.related_nodes.append(curnode)
            self.walked.add(curnode)
            curnode = self.parent_dic[curnode]

# @lc code=end

