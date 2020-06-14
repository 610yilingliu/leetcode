#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n):
        nums = [str(i) for i in range(0, 10)]
        self.ans = 0
        for mx_l in range(1, n + 1):
            self.generator(nums, '', mx_l)
        # plus zero itself
        return self.ans + 1
    def generator(self, nums, path, max_l):
        if len(path) == max_l:
            self.ans += 1
            return
        if not path:
            for i in range(1, len(nums)):
                self.generator(nums[:i] + nums[i + 1:], path + nums[i], max_l)
        else:
            for i in range(len(nums)):
                self.generator(nums[:i] + nums[i + 1:], path + nums[i], max_l)

# if __name__ == '__main__':
#     a = Solution()
#     b = a.countNumbersWithUniqueDigits(2)
#     print(b)
# @lc code=end

