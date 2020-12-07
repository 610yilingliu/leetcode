#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
# class Solution:
#     def addBinary(self, a: str, b: str):
#         a_l = len(a)
#         b_l = len(b)
#         if a_l > b_l:
#             b = "0" * (a_l - b_l) + b
#         elif b_l > a_l:
#             a = "0" * (b_l - a_l) + a
#         return self.addtwo(a, b)
    
#     def addtwo(self, num1, num2):
#         prev = 0
#         res = ""
#         for i in range(len(num1) - 1, -1, -1):
#             curnum = int(num1[i]) + int(num2[i]) + prev
#             if curnum == 2:
#                res = "0" + res
#                prev = 1
#             elif curnum == 3:
#                 res = "1" + res
#                 prev = 1
#             else:
#                 res = str(curnum) + res
#                 prev = 0
#         if prev:
#             res = str(prev) + res
#         return res

class Solution:
    def addBinary(self, a, b):
        longer = a if len(a) > len(b) else b
        if longer == a: 
            shorter = b
        else:
            shorter = a
        extra_zeros = len(longer) - len(shorter)
        shorter = '0' * extra_zeros + shorter
        ans = ""
        pre = 0
        for i in range(len(longer) - 1, -1, -1):
            if int(shorter[i]) + int(longer[i]) + pre == 3:
                ans = '1' + ans
                pre = 1
            elif int(shorter[i]) + int(longer[i]) + pre == 2:
                ans = '0' + ans
                pre = 1
            elif int(shorter[i]) + int(longer[i]) + pre == 1:
                ans = '1' + ans
                pre = 0
            else:
                ans = '0' + ans
                pre = 0
        if pre:
            ans = '1' + ans
        return ans


# @lc code=end

