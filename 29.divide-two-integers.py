#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend, divisor):
        if abs(divisor) >abs(dividend):
            return 0
        count = 0
        label = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            label = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = self.helper(dividend, divisor, 0, 0, 0)
        if label == 0:
            res = -res
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if res < - 2 ** 31:
            return - 2 ** 31
        return res


    def helper(self, dividend, divisor, current_s, count, temp_count):
        # stop recursion
        if dividend < divisor:
            return count
        # stop recursion
        if dividend == divisor:
            return count + 1
        # init
        if current_s == 0:
            current_s = divisor
        # init
        if temp_count == 0:
            temp_count = 1
        #  if current divisor (names temp count) * 2 is larger than dividend, than in next loop, try future divisor = current divisor * 2
        if dividend > current_s + current_s:
            return self.helper(dividend - current_s - current_s, divisor, current_s + current_s, count + temp_count + temp_count, temp_count + temp_count)
        # if above step fail
        if dividend > current_s:
            return self.helper(dividend - current_s, divisor, current_s, count + temp_count, temp_count)
        # else divisor start from the base divisor
        if dividend > divisor:
            return self.helper(dividend - divisor, divisor, divisor, count + 1, 1)
        
        
        
if __name__ == '__main__':
    a = Solution()
    b = a.divide(5, 1)
    print(b)
# @lc code=end

