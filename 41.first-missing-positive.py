#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums):
        if nums == []:
            return 1
        l = len(nums) + 1
        for i in range(1, l):
            if i not in nums:
                return i
        return l
# @lc code=end
if __name__ == '__main__':
    a = Solution()
    b = a.firstMissingPositive([7,8,9,11,12])
    print(b)