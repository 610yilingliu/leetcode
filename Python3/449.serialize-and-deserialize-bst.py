#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import collections
class Codec:
    
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        queue = collections.deque([root])
        res = ""
        while queue:
            cur = queue.popleft()
            if cur is not None:
                res = res + ',' + str(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res = res + ',' + '-'
        return res[1:]
            

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        tree_ls = data.split(',')
        if not tree_ls or not tree_ls[0]:
            return None
        root = TreeNode(int(tree_ls[0]))
        queue = collections.deque([root])
        cur = 1
        while cur < len(tree_ls):
            node = queue.popleft()
            if node is not None:
                node.left = TreeNode(int(tree_ls[cur])) if tree_ls[cur] != '-' else None
                queue.append(node.left)
                if cur + 1 < len(tree_ls):
                    node.right = TreeNode(int(tree_ls[cur + 1])) if tree_ls[cur + 1] != '-' else None
                    queue.append(node.right)
                    cur += 1
                cur += 1
        return root

# class Codec:
    
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#         :type root: TreeNode
#         :rtype: str
#         """
#         vals = []
#         def preOrder(root):
#             if root:
#                 vals.append(root.val)
#                 preOrder(root.left)
#                 preOrder(root.right)
#         preOrder(root)
#         return ' '.join(map(str, vals))


#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#         :type data: str
#         :rtype: TreeNode
#         """
#         vals = collections.deque(int(val) for val in data.split())
#         def build(minVal, maxVal):
#             if vals and minVal < vals[0] < maxVal:
#                 val = vals.popleft()
#                 root = TreeNode(val)
#                 root.left = build(minVal, val)
#                 root.right = build(val, maxVal)
#                 return root
#         return build(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

