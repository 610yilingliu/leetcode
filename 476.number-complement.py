#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int):
        ans = 0
        cnt = 0
        while num > 0:
            curhead = (num & 1) ^ 1
            num = num >> 1
            ans = (curhead << cnt) + ans
            cnt += 1
        return ans

# if __name__ == '__main__':
#     a = Solution()
#     b = a.findComplement(5)
#     print(b)
# @lc code=end

