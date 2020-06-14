#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s, k):
        if k > len(s):
            return len(s)
        counter = [0 for _ in range(26)]
        ans = k
        deleted = 0
        for i in range(len(s)):
            counter[ord(s[i]) - ord('A')] += 1
            largest = max(counter)
            if largest + k < i - deleted + 1:           
                counter[ord(s[deleted]) - ord('A')] -= 1
                deleted += 1
            ans = max(ans, i - deleted + 1)
        return ans
    # def characterReplacement(self, s, k):
    #     maxf = res = 0
    #     count = collections.Counter()
    #     for i in range(len(s)):
    #         count[s[i]] += 1
    #         maxf = max(maxf, count[s[i]])
    #         if res - maxf < k:
    #             res += 1
    #         else:
    #             count[s[i - res]] -= 1
    #     return res

if __name__ == '__main__':
    a = Solution()
    b = a.characterReplacement("AABA", 0)
    print(b)
# @lc code=end

