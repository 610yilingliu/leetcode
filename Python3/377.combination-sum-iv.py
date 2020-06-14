#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
# class Solution:
#     def combinationSum4(self, nums, target):
#         self.ans = 0
#         self.paths = []
#         for number in nums:
#             self.findpath(target - number, number, nums, [])
#         return self.ans

#     def findpath(self, rest, curnum, nums, path):
#         if rest < 0:
#             return
#         if rest == 0:
#             self.ans += 1
#             if path in self.paths:
#                 print(1)
#             self.paths.append(path)
#             return
#         for num in nums:
#             self.findpath(rest - num, num, nums, path + [num])

class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]

        
# if __name__ == '__main__':
#     a = Solution()
#     b = a.combinationSum4([4, 2, 1], 16)
#     print(b)
# @lc code=end

