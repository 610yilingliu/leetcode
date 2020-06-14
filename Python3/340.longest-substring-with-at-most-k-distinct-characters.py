#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        longest, start, distinct_count, visited = 0, 0, 0, [0 for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == 0:
                distinct_count += 1
            visited[ord(char)] += 1
             
            while distinct_count > k:
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1
   
            longest = max(longest, i - start + 1)
        return longest



# @lc code=end

