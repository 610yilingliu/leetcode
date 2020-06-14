#
# @lc app=leetcode id=266 lang=python3
#
# [266] Palindrome Permutation
#

# @lc code=start
import collections

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = collections.Counter(s)
        c = 0
        for k, v in d.items():
            if v & 1:
                if c > 0:
                    return False
                c += 1
        return True
# @lc code=end

