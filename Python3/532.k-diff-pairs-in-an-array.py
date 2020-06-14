#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start

import collections

class Solution:
    def findPairs(self, nums, k):
        if k == 0:
            counter = collections.Counter(nums)
            ans = 0
            for k in counter:
                if counter[k] > 1:
                    ans += 1
            return ans
            
        nums = list(set(nums))
        nums.sort()
        ans = 0
        i = 0
        j = 1
        while i < j and j < len(nums):
            if nums[j] - nums[i] < k:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
                if i == j:
                    j += 1
            else:
                if nums[j] - nums[i] == k:
                    ans += 1
                    i += 1
                    j += 1
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.findPairs([1, 2, 3, 4, 5], k = 1)
    print(b)

# @lc code=end

