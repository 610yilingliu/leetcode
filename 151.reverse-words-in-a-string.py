#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s):
        s = s.split()
        s = reversed(s)
        return ' '.join(s)

if __name__ == '__main__':
    a = Solution()
    b = a.reverseWords("a good   example")
    print(b)
# @lc code=end

