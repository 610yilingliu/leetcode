#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 10 and x >= 0:
            return True
        if x < 0 or x%10 == 0:
            return False
        right = 0
        while x > right and x >= 10:
            r = x%10
            x = x//10
            right = right * 10 + r 
        if right == x:
            return True
        elif right//10 == x:
            return True
        return False


if __name__ == '__main__':
    a = Solution()
    b = a.isPalindrome(21120)
    print(b)
# @lc code=end

