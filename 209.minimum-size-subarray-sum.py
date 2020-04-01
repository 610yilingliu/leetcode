#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        if nums[0] >= s:
            return 1
        l = 0
        r = 1
        ans = float('inf')
        while r < len(nums) and l < r:
            if nums[r] >= s:
                return 1
            while r < len(nums) and sum(nums[l: r + 1]) < s:
                r += 1
            while l < r and sum(nums[l: r + 1]) > s:
                l += 1
            if sum(nums[l: r + 1]) < s:
                l -= 1
            if sum(nums[l: r + 1])  >= s:
                ans = min(ans, r + 1 - l)
            l += 1
        if ans != float('inf'):
            return ans
        return 0

if __name__ == '__main__':
    a = Solution()
    b = a.minSubArrayLen(11, [1,2,3,4,5])
    print(b)


# @lc code=end

