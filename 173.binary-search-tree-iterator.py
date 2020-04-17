#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root):
        self.valls = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.valls.append(root)
            root = root.right
        self.cur = -1

    def next(self):
        """
        @return the next smallest number
        """
        self.cur += 1
        if self.cur < len(self.valls):
            return self.valls[self.cur].val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        if self.cur < len(self.valls) - 1:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

