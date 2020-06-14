#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s):
        if not s:
            return []
        self.ans = []
        self.helper(s, [])
        return self.ans

    def helper(self, s, path):
        if not s and path != []:
            self.ans.append(path)
        for i in range(1, len(s) + 1):
            if self.is_partition(s[:i]):
                self.helper(s[i:], path + [s[:i]])


    def is_partition(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    a = Solution()
    b = a.partition("aab")
    print(b)
# @lc code=end

