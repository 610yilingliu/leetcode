#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num, k):
        if len(num) == k:
            return "0"
        ans = self.recursion(num, k)
        return ans

    def recursion(self, num, k):
        if k == 0:
            return str(int(num))
        i = 0
        while i < len(num) - 1 and num[i] <= num[i + 1]:
            i += 1
        num = num[:i] + num[i + 1:]
        return self.removeKdigits(num, k - 1)       
        

if __name__ == '__main__':
    a = Solution()
    b = a.removeKdigits("112", 1)
    print(b)

# @lc code=end

