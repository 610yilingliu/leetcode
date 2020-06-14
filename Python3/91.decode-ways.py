#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            if s[0] == '0':
                return 0
            return 1
        if len(s) == 2:
            if s[0] == '0':
                return 0
            if int(s) == 10 or int(s) == 20 or (int(s) > 26 and s[1] != '0'):
                return 1
            if s[1] == '0' and s[0] > '2':
                return 0
            return 2
        dp = [0] * (len(s) + 1)        
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(dp)):
            if int(s[i - 2:i]) == 10 or int(s[i - 2:i]) == 20:
                dp[i] = dp[i - 2]
            elif 9 < int(s[i - 2 : i]) < 27 and s[i - 1]!='0':
                dp[i] = dp[i-1] +dp[i - 2]
            elif s[i - 1] != '0':
                dp[i] = dp[i - 1]
            else:
                return 0
        return dp[-1]




if __name__ == '__main__':
    a = Solution()
    b = a.numDecodings('30')
    print(b)


# @lc code=end

