#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    # def isAnagram(self, s: str, t: str):
    #     if len(s) != len(t):
    #         return False
    #     d = dict()
    #     l = len(s)
    #     for i in range(l):
    #         if s[i] not in d:
    #             d[s[i]] = 1
    #         else:
    #             d[s[i]] += 1
    #     for i in range(l):
    #         if t[i] not in d:
    #             return False
    #         else:
    #             if d[t[i]] == 1:
    #                 d.pop(t[i])
    #             else:
    #                 d[t[i]] -= 1
    #     if len(d) == 0:
    #         return True
    #     return False

    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

if __name__ == '__main__':
    a = Solution()
    b = a.isAnagram("anagram", "nagaram")
    print(b)

# @lc code=end

