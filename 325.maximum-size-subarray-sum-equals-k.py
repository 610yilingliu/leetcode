#
# @lc app=leetcode id=325 lang=python3
#
# [325] Maximum Size Subarray Sum Equals k
#

# @lc code=start
class Solution:
    def maxSubArrayLen(self, nums, k):
        sums = dict()
        ans = 0
        cursum = 0
        for i in range(len(nums)):
            cursum += nums[i]
            if cursum == k:
                ans = i + 1
            elif cursum - k in sums:
                ans = max(ans, i - sums[cursum - k])
            if cursum not in sums:
                sums[cursum] = i
        return ans


# if __name__ == '__main__':
#     a = Solution()
#     b = a.maxSubArrayLen([1, 1, 0], 1)
#     print(b)


# @lc code=end

