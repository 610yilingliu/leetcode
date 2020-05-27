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

if __name__ == '__main__':
    a = tree_builder([1,None,2,2])
    print(a)