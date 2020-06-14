#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1, s2):
        # s1: target
        # s2: pool
        p = 0
        win = len(s1)
        s1 = sorted(list(s1))
        while p + win <= len(s2):
            current_str = s2[p : p + win]
            ls = sorted(list(current_str))
            if ls == s1:
                return True
            p += 1
        return False


if __name__ == '__main__':
    a = Solution()
    b = a.checkInclusion("adc", "dcda")
    print(b)
# @lc code=end

