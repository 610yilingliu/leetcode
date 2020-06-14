#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
class Solution:
    def minCut(self, s):
        if not s or len(s) == 1:
            return 0
            
        helper = [i for i in range(len(s) + 1)]
        for i in range(len(s)):
            for j in range(i):
                if self.is_pa(s[j: i + 1]):
                    helper[i + 1] = min(helper[i + 1], helper[j] + 1)
            helper[i + 1] = min(helper[i + 1], helper[i] + 1)
        return helper[-1] - 1

    def is_pa(self, string):
        return string == string[::-1]

if __name__ == '__main__':
    a = Solution()
    b = a.minCut("aab")
    print(b)
# @lc code=end

