#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s):
        ans = 0
        p = 0
        for i in range(len(s) - 1, -1, -1):
            cur = 26 ** p  * (ord(s[i]) - ord('A') + 1)
            ans = cur + ans
            p += 1
        return ans
if __name__ == '__main__':
    a = Solution()
    b = a.titleToNumber('BA')
    print(b)
# @lc code=end

