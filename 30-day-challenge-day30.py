class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def bstFromPreorder(self, preorder):
    #     if not preorder:
    #         return None
    #     preorder.sort()
    #     root = self.generator(1, preorder)
    #     return root

    # def generator(self, idx, preorder):
    #     mx = len(preorder)
    #     if idx > mx:
    #         return None
    #     node = TreeNode(preorder[idx - 1])
    #     if mx - 1 == idx << 1:
    #         if preorder[idx - 1] > preorder[-1]:
    #             node.left = TreeNode(preorder[-1])
    #         else:
    #             node.right = TreeNode(preorder[-1])
    #     else:
    #         next_l = idx << 1
    #         node.left = self.generator(next_l, preorder)
    #         next_r = (idx << 1) + 1
    #         node.right = self.generator(next_r, preorder)
    #     return node

    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        inorder = sorted(preorder)
        def generator(preorder, inorder):
            if not preorder or not inorder:
                return None
            node = TreeNode(preorder[0])
            inorder_idx = inorder.index(preorder[0])
            node.left = generator(preorder[1:inorder_idx + 1], inorder[:inorder_idx])
            node.right = generator(preorder[inorder_idx + 1:], inorder[inorder_idx + 1:])
            return node
        return generator(preorder, inorder)
        


if __name__ == '__main__':
    a = Solution()
    b = a.bstFromPreorder([1,3])
    print(b)