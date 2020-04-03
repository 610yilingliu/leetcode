#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str):
        d = dict()
        l = len(s)
        for i in range(l):
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        s = list(s)
        t = list(t)
        return len(set(s)) == len(set(t))

if __name__ == '__main__':
    a = Solution()
    b = a.isIsomorphic("paper","title")
    print(b)


                




# @lc code=end

