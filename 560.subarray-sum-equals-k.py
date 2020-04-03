#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums, k):
        # subarraySum(self, nums: List[int], k: int) -> int

        # special return conditions
        if not nums:
            return 0
        if len(nums) == 1:
            if nums[0] != k:
                return 0
            return 1
        # initialize
        sums = {0:1}
        ans = 0
        # sum
        s = 0
        for item in nums:
            s += item
            if s - k in sums:
                ans += sums[s - k]
            sums[s] = sums.get(s, 0) + 1
        return ans

        
        
if __name__ == '__main__':
    a = Solution()
    b = a.subarraySum([1,1,1], k = 2)
    print(b)

        
# @lc code=end

