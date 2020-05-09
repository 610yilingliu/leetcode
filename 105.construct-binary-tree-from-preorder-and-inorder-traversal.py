#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        node = TreeNode(preorder[0])
        inorder_idx = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:inorder_idx + 1], inorder[:inorder_idx])
        node.right = self.buildTree(preorder[inorder_idx + 1:], inorder[inorder_idx + 1:])
        return node


if __name__ == '__main__':
    a = Solution()
    b = a.buildTree([3,9,20,15,7], [9,3,15,20,7])
    print(b)
# @lc code=end


        