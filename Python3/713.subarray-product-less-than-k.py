#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
import collections

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if len(nums) == 1:
            if nums[0] < k:
                return 1
            return 0
        mult = 1
        l = 0
        r = 0
        ans = 0
        for r in range(len(nums)):
            mult *= nums[r]
            while l <= r and mult >= k:          
                mult //= nums[l]
                l += 1
            ans += r - l + 1
        return ans
            

if __name__ == '__main__':
    a = Solution()
    b = a.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
    print(b)


# @lc code=end

