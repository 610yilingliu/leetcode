#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
class node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
        self.smallernum = 0
class Solution:
    def countSmaller(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [0]
        self.ans = [0] * len(nums)
        root = None
        for idx, val in enumerate(nums[::-1]):
            root = self.insert(root, val, idx)
        return self.ans[::-1]

    def insert(self, root, val, idx):
        if not root:
            root = node(val)
        elif root.val >= val:
            root.smallernum += 1
            root.left = self.insert(root.left, val, idx)
        elif root.val < val:
            self.ans[idx] += root.smallernum + 1
            root.right = self.insert(root.right, val, idx)
        return root


# if __name__ == '__main__':
#     a = Solution()
#     b = a.countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41])
#     print(b)
# @lc code=end

