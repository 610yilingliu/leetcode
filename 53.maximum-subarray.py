#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        current = nums[0]
        ans = nums[0]
        for num in nums[1:]:
            current = max(current + num, num)
            ans = max(ans, current)
        return ans

if __name__=='__main__':
    a = Solution()
    b = a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(b)




# @lc code=end

