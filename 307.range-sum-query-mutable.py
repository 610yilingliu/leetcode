#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
# https://www.jianshu.com/p/8fe5ae822f93
class segnode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.s = 0
        self.left = None
        self.right = None

class NumArray:

    def __init__(self, nums):
        def tree_helper(l, r):
            if l > r:
                return None
            if l == r:
                node = segnode(l, r)
                node.s = nums[l]
                return node
            mid = (l + r) // 2
            root = segnode(l, r)
            root.left, root.right = tree_helper(l, mid), tree_helper(mid + 1, r)
            root.s = root.left.s + root.right.s
            return root
        self.root = tree_helper(0, len(nums) - 1)    

    def update(self, i: int, val: int):
        def updater(root, i, val):
            if root.start == root.end:
                root.s = val
                return val
            mid = (root.start + root.end)//2
            if i <= mid:
                updater(root.left, i, val)
            else:
                updater(root.right, i, val)
            root.s = root.left.s + root.right.s
            return root.s

        updater(self.root, i, val)
            


    def sumRange(self, i: int, j: int):
        def finder(root, l, r):
            if root.start == l and root.end == r:
                return root.s
            mid = (root.start + root.end)//2
            if r <= mid:
                return finder(root.left, l, r)
            if l > mid:
                return finder(root.right, l, r)
            return finder(root.left, l, mid) + finder(root.right, mid + 1, r)

        return finder(self.root, i, j)

        


# Your NumArray object will be instantiated and called as such:
obj = NumArray([9,-8])
obj.update(0,3)
a = obj.sumRange(1,1)
b = obj.sumRange(0, 1)
obj.update(1,-3)
c = obj.sumRange(0,1)
# @lc code=end

