#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#

# @lc code=start
class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        ln=len(str(n))
        if ln==1:
            return 1 
        tmp1=10**(ln-1)
        firstnum=n//tmp1
        Fone = n%tmp1+1 if firstnum==1 else tmp1
        other = firstnum*(ln-1)*(tmp1//10)
        return Fone + other + self.countDigitOne(n % tmp1)
# @lc code=end

