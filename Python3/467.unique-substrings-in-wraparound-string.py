#
# @lc app=leetcode id=467 lang=python3
#
# [467] Unique Substrings in Wraparound String
#
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/
#
# algorithms
# Medium (35.14%)
# Likes:    600
# Dislikes: 86
# Total Accepted:    25.3K
# Total Submissions: 70.9K
# Testcase Example:  '"a"'
#
# Consider the string s to be the infinite wraparound string of
# "abcdefghijklmnopqrstuvwxyz", so s will look like this:
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
# 
# Now we have another string p. Your job is to find out how many unique
# non-empty substrings of p are present in s. In particular, your input is the
# string p and you need to output the number of different non-empty substrings
# of p in the string s.
# 
# Note: p consists of only lowercase English letters and the size of p might be
# over 10000.
# 
# Example 1:
# 
# Input: "a"
# Output: 1
# 
# Explanation: Only the substring "a" of string "a" is in the string s.
# 
# 
# 
# Example 2:
# 
# Input: "cac"
# Output: 2
# Explanation: There are two substrings "a", "c" of string "cac" in the string
# s.
# 
# 
# 
# Example 3:
# 
# Input: "zab"
# Output: 6
# Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of
# string "zab" in the string s.
# 
# 
#
# @lc code=start
# class Solution:
#     def findSubstringInWraproundString(self, p: str):
#         def loc(char):
#             return ord(char) - ord('a')
#         storage = [0] * 26
#         shift = dict()
#         visited = set()
#         for i in range(len(p)):
#             char = p[i]
#             charloc = loc(char)
#             if char not in shift:
#                 storage[charloc] += 1
#                 shift[char] = 0
#                 visited.add(char)
#             if i + shift[char] < len(p) - 1 and p[i:i + shift[char] + 1] in visited:
#                 for j in range(i + shift[char] + 1, len(p)):
#                     if ord(p[j]) - ord(p[j - 1]) == 1 or (p[j] == 'a' and p[j - 1] == 'z'):
#                         shift[char] += 1
#                         storage[charloc] += 1
#                         visited.add(p[i: j + 1])
#                     else:
#                         break
#         return sum(storage)
class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        count = collections.defaultdict(int)
        N = len(p)
        _len = 0
        for i in range(N):
            if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or (p[i] == 'a' and p[i - 1] == 'z')):
                _len += 1
            else:
                _len = 1
            count[p[i]] = max(count[p[i]], _len)
        return sum(count.values())
# if __name__ == '__main__':
#     a = Solution()
#     b = a.findSubstringInWraproundString("zab")
#     print(b)
            


# @lc code=end

