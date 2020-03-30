#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s):
        # lowercase = chr(ord(uppercase) - 32)
        # lower: 97-122
        # upper: 65-90
        # 0-9: 48 - 57
        l = 0
        r = len(s) - 1
        s = list(s)
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif (48 <= ord(s[l]) <= 57 or 97 <= ord(s[l]) <= 122) and (48 <= ord(s[r]) <= 57 or 97 <= ord(s[r]) <= 122) and s[l] != s[r]:
                return False
            else:
                # not belong to letters
                if ord(s[l]) < 48 or 57 < ord(s[l]) < 65 or 90 < ord(s[l]) < 97 or ord(s[l]) > 122:
                    l += 1
                if ord(s[r]) < 48 or 57 < ord(s[r]) < 65 or 90 < ord(s[r]) < 97 or ord(s[r]) > 122:
                    r -= 1
                if 65 <= ord(s[l]) <= 90:
                    s[l] = chr(ord(s[l]) + 32)
                if 65 <= ord(s[r]) <= 90:
                    s[r] = chr(ord(s[r]) + 32)
        return True

if __name__ == '__main__':
    a = Solution()
    b = a.isPalindrome("A man, a plan, a canal: Panama")
    print(b)
                
# @lc code=end

