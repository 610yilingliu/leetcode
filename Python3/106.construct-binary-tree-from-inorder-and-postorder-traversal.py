#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        node = TreeNode(postorder[-1])
        inorder_idx = inorder.index(postorder[-1])
        node.left = self.buildTree(inorder[:inorder_idx], postorder[:inorder_idx])
        node.right = self.buildTree(inorder[inorder_idx + 1:], postorder[inorder_idx: len(postorder) - 1])
        return node


if __name__ == '__main__':
    a = Solution()
    b = a.buildTree([9,3,15,20,7], [9,15,7,20,3])
    print(b)
# @lc code=end

