#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return []
        length = len(nums)
        helper_l, helper_r  = [1] * length, [1] * length
        for i in range(1, length):
            helper_l[i] = helper_l[i - 1] * nums[i - 1]
        for j in range(length - 2, -1, -1):
            helper_r[j] = helper_r[j + 1] * nums[j + 1]
        ans = []
        for i in range(length):
            ans.append(helper_l[i] * helper_r[i])
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.productExceptSelf([1,2,3,4])
    print(b)
# @lc code=end

