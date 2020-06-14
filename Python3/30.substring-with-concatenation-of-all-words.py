#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
import collections

class Solution:
    def findSubstring(self, s, words):
        if not words or not s:
            return []
        ans = []
        l = len(words[0])
        window = l * len(words)
        idx = 0
        words = collections.Counter(words)
        while idx + window <= len(s):
            temp = words.copy()
            cur_window = s[idx:idx + window]
            for i in range(0, window, l):
                current = cur_window[i:i+l]
                if current in temp:
                    if temp[current] > 1:
                        temp[current] -= 1
                    else:
                        temp.pop(current)
                else:
                    break
            if not temp:
                ans.append(idx)
            idx += 1
        return ans


if __name__ == '__main__':
    a = Solution()
    b = a.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
    print(b)

# @lc code=end

