#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#

# @lc code=start
class Solution:
    def reverseWords(self, s: List[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        def reversor(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        reversor(0, len(s) - 1)
        pre = 0
        for idx in range(len(s)):
            if s[idx] == ' ':
                reversor(pre, idx - 1)
                pre = idx + 1
        reversor(pre, len(s) - 1)

        
# @lc code=end

