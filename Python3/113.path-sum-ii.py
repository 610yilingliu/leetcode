#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
import collections

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
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, s):
        if not root:
            return []
        ans = []
        target = s
        def finder(root, path):
            if sum(path) == target and not root.left and not root.right:
                ans.append(path)
            if root.left:
                finder(root.left, path + [root.left.val])
            if root.right:
                finder(root.right, path + [root.right.val])
        finder(root, [root.val])
        return ans

if __name__ == '__main__':
    t = construct_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    a = Solution()
    b = a.pathSum(t, 22)
    print(b)

# @lc code=end

