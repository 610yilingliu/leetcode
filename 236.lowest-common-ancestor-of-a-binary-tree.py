#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = collections.deque([root])
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

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         targets = {p, q}
#         conn = collections.defaultdict(TreeNode)
#         def traveller(root, targets):
#             if not targets:
#                 return
#             if root.left:
#                 conn[root.left] = root
#                 if root.left in targets:
#                     targets.remove(root.left)
#                 traveller(root.left, targets)
#             if root.right:
#                 conn[root.right] = root
#                 if root.right in targets:
#                     targets.remove(root.right)
#                 traveller(root.left, targets)
#         traveller(root, targets)
#         # linked list intersaction
#         phead = p
#         qhead = q
#         intersection= None
#         while phead != qhead:
#             if phead in conn:
#                 if phead == q:
#                     intersection = q
#                     break
#                 phead = conn[phead]
#             else:
#                 phead = q

#             if qhead in conn:
#                 if qhead == p:
#                     intersection = p
#                     break
#                 qhead = conn[qhead]              
#             else:
#                 qhead = p
#         if intersection is None:
#             intersection = phead
#         ls = []
#         if intersection not in conn:
#             return intersection
#         else:
#             while intersection in conn:
#                 ls.append([intersection.val, intersection])
#                 intersection = conn[intersection]
#             ls.sort()
#             return ls[0][1]

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root or root == p or root == q:
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            
            if left and right: #一个在左子树，一个在右子树
                return root
            elif left:#都在左子树
                return left
            elif right:#都在右子树
                return right
            else:
                return


# @lc code=end
