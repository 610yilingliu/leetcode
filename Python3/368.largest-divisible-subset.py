#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        dp = [1 for i in range(len(nums))]
        val = [[i] for i in nums]
        maxInx = 0
        maxV = 0
        for i, v in enumerate(dp):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        l = val[j][:]
                        l.append(nums[i])
                        val[i] = l
                        dp[i] = dp[j] + 1
                        if maxV < len(val[i]):
                            maxInx = i
                            maxV = len(val[i])
        return val[maxInx]

# if __name__ == '__main__':
#     a = Solution()
#     b = a.largestDivisibleSubset([1,2,4,8,16])
#     print(b)
# @lc code=end

