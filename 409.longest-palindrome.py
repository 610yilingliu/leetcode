#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

import collections
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str):
        if not s:
            return 0
        char_nums = collections.Counter(s)
        ans = 0
        odd = False
        for k in char_nums:
            if char_nums[k] & 1 == 0:
                ans += char_nums[k]
            else:
                if char_nums[k] > 1:
                    ans += char_nums[k] - 1
                odd = True
        if odd == True:
            return ans + 1
        return ans



# @lc code=end

