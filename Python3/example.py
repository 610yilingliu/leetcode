import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def tree_builder(values):
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



tree = [1, 2, 3, 4, 5, 6]
tree = tree_builder(tree)
print(tree)


class Solution:
    def preorderTraversal_1(self, root):
        q = []
        ans = []
        while q or root:
            while root:
                ans.append(root.val)
                q.append(root)
                root = root.left
            root = q.pop()
            root = root.right
        return ans

    def preorderTraversal_2(self, root):
        self.ans = []
        # def preorder(node):
        #     if not node:
        #         return None
        #     ans.append(node.val)
        #     preorder(node.left)
        #     preorder(node.right)

        # preorder(root)
        self.preorder(root)
        return self.ans


    def preorder(self, node):
        if not node:
            return None
        self.ans.append(node.val)
        self.preorder(node.left)
        self.preorder(node.right)

ans = Solution()
a = ans.preorderTraversal_2(tree)
print(a)