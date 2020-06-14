#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
# if __name__ == '__main__':
#     a = Solution()
#     b = a.increasingTriplet([1,2,3,4,5])
#     print(b)
# @lc code=end

