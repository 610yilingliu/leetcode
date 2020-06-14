#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution():
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ""
        left, cnt, minLen = 0, 0, float('inf')
        count = collections.Counter(t)
        for i, c in enumerate(s):
            count[c] -= 1
            if count[c] >= 0:
                cnt += 1
            while cnt == len(t):
                if minLen > i - left + 1:
                    minLen = i - left + 1
                    res = s[left : i + 1]
                count[s[left]] += 1
                if count[s[left]] > 0:
                    cnt -= 1
                left += 1
        return res
            
# @lc code=end

