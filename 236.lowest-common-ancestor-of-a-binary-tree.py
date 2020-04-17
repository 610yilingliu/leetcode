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

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        targets = {p, q}
        conn = collections.defaultdict(TreeNode)
        def traveller(root, targets):
            if not targets:
                return
            if root.left:
                conn[root.left] = root
                if root.left in targets:
                    targets.remove(root.left)
                traveller(root.left, targets)
            if root.right:
                conn[root.right] = root
                if root.right in targets:
                    targets.remove(root.right)
                traveller(root.left, targets)
        traveller(root, targets)
        # linked list intersaction
        phead = p
        qhead = q
        intersection= None
        while phead != qhead:
            if phead in conn:
                phead = conn[phead]
                if phead == q:
                    intersection = q
                    break
            else:
                phead = q

            if qhead in conn:
                qhead = conn[qhead]
                if qhead == p:
                    intersection = p
                    break               
            else:
                qhead = p
        if intersection is None:
            intersection = phead
        ls = []
        if intersection not in conn:
            return intersection
        else:
            while intersection in conn:
                ls.append([intersection.val, intersection])
                intersection = conn[intersection]
            ls.sort()
            return ls[0][1]

# @lc code=end


if __name__ == '__main__':
    tree = construct_tree([3,5,1,6,2,0,8,None,None,7,4])
    v1 = TreeNode(5)
    v2 = TreeNode(1)
    a = Solution()
    b = a.lowestCommonAncestor(tree, v1, v2)
    print(b)