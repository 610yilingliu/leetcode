#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
import collections

class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p) or not s or not p:
            return []
        rg = len(p)
        pd = collections.Counter(p)
        # initialize
        sd = collections.Counter(s[:rg])
        ans = []
        if pd == sd:
            ans = [0]
        for pos in range(1, len(s) - rg + 1):
            if sd[s[pos - 1]] == 1:
                sd.pop(s[pos - 1])
            else:
                sd[s[pos - 1]] -= 1
            if s[pos + rg - 1] not in sd:
                sd[s[pos + rg - 1]] = 1
            else:
                sd[s[pos + rg - 1]] += 1
            if pd == sd:
                ans.append(pos)
            pos += 1
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.findAnagrams("abab", "ab")
    print(b)


# @lc code=end

