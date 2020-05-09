#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

# @lc code=start
import heapq

class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        # is there k or more distance greater/equal to the give input?
        def guess(cutpoint):
            # count the number of distances
            counter = 0
            curleft = 0
            for i in range(len(nums)):
                while nums[i] - nums[curleft] > cutpoint:
                    curleft += 1
                counter += i - curleft
            if counter >= k:
                return True
            return False
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if guess(mid):
                right = mid
            else:
                left  = mid + 1
        return left
# class Solution(object):
#     def smallestDistancePair(self, nums, k):
#         def possible(guess):
#             #Is there k or more pairs with distance <= guess?
#             count = left = 0
#             for right, x in enumerate(nums):
#                 while x - nums[left] > guess:
#                     left += 1
#                 count += right - left
#             return count >= k

#         nums.sort()
#         lo = 0
#         hi = nums[-1] - nums[0]
#         while lo < hi:
#             mi = (lo + hi) // 2
#             if possible(mi):
#                 hi = mi
#             else:
#                 lo = mi + 1

#         return lo
# @lc code=end

