#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) < 2:
            return len(nums)
        dp = [1] * len(nums)
        mx = dp[0]
        for i in range(1, len(nums)):
            temp = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    temp  = max(temp, dp[j])
            dp[i] = temp + 1
            mx = max(mx, dp[i])
        return mx

if __name__ == '__main__':
    a = Solution()
    b = a.lengthOfLIS([1,3,6,7,9,4,10,5,6])
    print(b)
# @lc code=end

