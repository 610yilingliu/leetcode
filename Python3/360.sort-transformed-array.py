#
# @lc app=leetcode id=360 lang=python3
#
# [360] Sort Transformed Array
#

# @lc code=start
class Solution():
    def sortTransformedArray(self, nums, a, b, c):
        if not nums:
            return []
        res = [0] * len(nums)
        i, j = 0, len(nums) - 1
        index = len(nums) - 1 if a >= 0 else 0
        while i <= j:
            if a >= 0:
                calc_i = self.calc(nums[i], a, b, c)
                calc_j = self.calc(nums[j], a, b, c)
                if  calc_i >= calc_j:
                    res[index] = calc_i
                    i += 1
                else:
                    res[index] = calc_j
                    j -= 1
                index -= 1
            else:
                calc_i = self.calc(nums[i], a, b, c)
                calc_j = self.calc(nums[j], a, b, c)
                if  calc_i <= calc_j:
                    res[index] = calc_i
                    i += 1
                else:
                    res[index] = calc_j
                    j -= 1
                index += 1
 
        return res


    def calc(self, x, a, b, c):
        return  a * x * x + b * x + c
# @lc code=end

