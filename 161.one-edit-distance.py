#
# @lc app=leetcode id=161 lang=python3
#
# [161] One Edit Distance
#

# @lc code=start
class Solution:
    def isOneEditDistance(self, s: str, t: str):
        if s == t:
            return False
        if abs(len(s) - len(t)) > 1:
            return False
        def repair(shorter, longer):
            shorter = shorter + ' '
            c = 0
            for i in range(len(longer)):
                if shorter[i]!= longer[i]:
                    if c > 0:
                        return False
                    shorter = shorter[:i] + longer[i] + shorter[i:]
                    c += 1
            return True
        if len(s) < len(t):
            return repair(s, t)
        if len(s) > len(t):
            return repair(t, s)
        counter = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                if counter > 0:
                    return False
                counter += 1
        return True

# if __name__ == '__main__':
#     a = Solution()
#     b = a.isOneEditDistance("a", '')
#     print(b)
        
# @lc code=end

