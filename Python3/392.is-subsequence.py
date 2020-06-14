#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        for i in range(len(t)):
            if s[0] == t[i]:
                return self.isSubsequence(s[1:], t[i + 1 :])
        return False

if __name__ == '__main__':
    a = Solution()
    b = a.isSubsequence("abc", "ahbgdc")
    print(b)
 # @lc code=end

