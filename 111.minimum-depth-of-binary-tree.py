#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
import collections
# define tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# main part
class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        l = self.minDepth(root.left) + 1
        r = self.minDepth(root.right) + 1
        if l == 1:
            return r
        if r == 1:
            return l
        return min(l, r)
# build the tree
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
    
# build instance, and test
if __name__ == '__main__':
    # build a tree from the list
    tree = tree_builder([3,9,20,None,None,15,7])
    # class instance, if you are a beginner of coding, please learn about class and method
    a = Solution()
    # use class method mindepth. This method receives a tree instead of the list you saw on leetcode webpage
    b = a.minDepth(tree)
    # show result
    print(b)

# @lc code=end

