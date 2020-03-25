#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n, k):
        self.ans = []
        nums = [num for num in range(1, n + 1)]
        if n == k:
            self.ans.append(nums)
            return self.ans
        else:
            ls = []
            self.helper(nums, k, ls)
            return self.ans


    def helper(self, array, k, current_ls):
        if k > len(array):
            return
        if k == 0:
            self.ans.append(current_ls)
        for i in range(len(array)):
            self.helper(array[i + 1:], k - 1, [array[i]] + current_ls)

# @lc code=end

