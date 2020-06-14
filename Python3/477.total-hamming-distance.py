#
# @lc app=leetcode id=477 lang=python3
#
# [477] Total Hamming Distance
#

# @lc code=start
# import collections

# class Solution:
#     def totalHammingDistance(self, nums):
#         onedict = collections.defaultdict(set)

#         def ones(num, curinput):
#             curdigit = 0
#             while curinput > 0:
#                 if curinput & 1 == 1:
#                     onedict[num].add(curdigit)
#                 curinput = curinput >> 1
#                 curdigit += 1

#         for num in nums:
#             if num not in onedict:
#                 ones(num, num)
#         distances = collections.defaultdict(int)
#         def dist_counter(num1, num2):
#             l1 = len(onedict[num1] & onedict[num2])
#             l2 = len(onedict[num1] | onedict[num2])
#             return l2 - l1
#         ans = 0
#         for i in range(len(nums) - 1):
#             distance = 0
#             num1 = nums[i]
#             for j in range(i + 1, len(nums)):
#                 num2 = nums[j]
#                 if num1 != num2:
#                     ans += dist_counter(num1, num2)
#         return ans
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for pos in range(32):
            bitCount = 0
            for i in range(len(nums)):
                bitCount += (nums[i] >> pos) & 1
            res += bitCount * (len(nums) - bitCount)
        return res

# if __name__ == '__main__':
#     a = Solution()
#     b = a.totalHammingDistance([4,14,4,14])
#     print(b)
# @lc code=end

