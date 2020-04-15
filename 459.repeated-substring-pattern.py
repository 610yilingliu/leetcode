#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s):
        for i in range(1, len(s)):
            cur = s[:i]
            if float(len(s)//len(cur)) == len(s)/len(cur):
                cur_stat = True
                for start in range(0, len(s), len(cur)):
                    if not s[start:].startswith(cur):
                        cur_stat = False
                        break
                if cur_stat:
                    return True
        return False

if __name__ == '__main__':
    a = Solution()
    b = a.repeatedSubstringPattern("abab")
    print(b)


# @lc code=end

