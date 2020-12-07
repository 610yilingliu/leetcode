#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
import collections


class Solution():
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # res = ""
        # left, cnt, minLen = 0, 0, float('inf')
        # count = collections.Counter(t)
        # for i, c in enumerate(s):
        #     count[c] -= 1
        #     if count[c] >= 0:
        #         cnt += 1
        #     while cnt == len(t):
        #         if minLen > i - left + 1:
        #             minLen = i - left + 1
        #             res = s[left : i + 1]
        #         count[s[left]] += 1
        #         if count[s[left]] > 0:
        #             cnt -= 1
        #         left += 1
        # return res
        res = ""
        chars = collections.Counter(t)
        found = 0
        mi = float('inf')
        lp = 0
        rp = 0
        while rp < len(s):
            chars[s[rp]] -= 1
            if chars[s[rp]] >= 0:
                found += 1
            while found == len(t):
                if mi > rp + 1 - lp:
                    mi = rp + 1 - lp
                    res = s[lp: rp + 1]
                chars[s[lp]] += 1
                if chars[s[lp]] > 0:
                    found -= 1
                lp += 1
            rp += 1
        return res


a = Solution()
b = a.minWindow("ADOBECODEBANC", "ABC")
print(b)
            
# @lc code=end

