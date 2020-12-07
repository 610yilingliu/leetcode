#
# @lc app=leetcode id=902 lang=python3
#
# [902] Numbers At Most N Given Digit Set
#

# @lc code=start
# - Generated number < n
# - Single digits only
# - Can we start with 0?
# - Sorted array?

# sol 1: backtrack, generate all possible answers and count the length of returned list, Time Spent: A(1, n) + A(2, n) + ... + A(len(n), n). Very slow way
class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: list[string], list with string of single digits
        :type n: int, maximum number to generate
        :rtype: int, number of generate numbers 
        """
        mx_len = len(str(n))
        self.ans = []
        self.max = n
        for i in range(1, mx_len):
            self.generate_nums("", 0, digits, i)
        return len(self.ans)

    def generate_nums(self, curstr, cur_cnt, digits, mx):
        if cur_cnt == mx:
            if int(curstr) < self.max:
                self.ans.append(curstr)
            return
        for i in range(len(digits)):
            # cannot start with 0
            if cur_cnt == 0 and digits[i] == '0':
                continue
            self.generate_nums(curstr + digits[i], cur_cnt + 1, digits, mx)
        
# sol 2
# class Solution:
#     def atMostNGivenDigitSet(self, digits, n):
#         up, ans, T, str_n = [0]*10, 0, len(digits), str(n)
#         for i in range(10):
#             for dig in digits:
#                 up[i] += (dig < str(i))
        
#         k, d_set = len(str_n), set(digits)
#         for i in range(k):
#             if i > 0 and str_n[i-1] not in d_set: break
#             ans += up[int(str_n[i])] * T**(k-i-1)
        
#         addon = (T**k - 1)//(T-1) - 1 if T != 1 else k - 1
#         return ans + addon + (not set(str_n) - set(digits))

if __name__ == '__main__':
    a = Solution()
    b = a.atMostNGivenDigitSet(["1","3","5","7"], 100)
    print(b)
# @lc code=end

