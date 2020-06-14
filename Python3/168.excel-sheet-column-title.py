#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, n):
        res = ''
        while n:
            num = (n - 1) % 26
            res = chr(ord('A') + num) + res
            n = (n - 1) // 26

        return res

if __name__ == '__main__':
    a = Solution()
    b = a.convertToTitle(52)
    print(b)
        
# @lc code=end

