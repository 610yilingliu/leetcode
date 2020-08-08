#
# @lc app=leetcode id=423 lang=python3
#
# [423] Reconstruct Original Digits from English
#

# @lc code=start
# class Solution:
#     def originalDigits(self, s):
#         numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
#         code = []

#         def count_alt(num):
#             alt = [0] * 26
#             for char in num:
#                 ascii_shift = ord(char) - ord('a')
#                 alt[ascii_shift] += 1
#             return alt

#         for number in numbers:
#             alt = count_alt(number)
#             code.append(alt)
#         string_alt = count_alt(s)
#         self.path = []
#         self.findpath(string_alt, code, [])
#         res_string = ""
#         for val in self.path:
#             for i in range(10):
#                 if code[i] == val:
#                     res_string += str(i)
#         return ''.join(sorted(res_string))

#     def findpath(self, string_alt, code_dict, path):
#         comp = [0] * 26
#         if string_alt == comp:
#             self.path = path
#             return
#         for item in string_alt:
#             if item < 0:
#                return
#         for num_code in code_dict:
#             nxt = []
#             for i in range(26):
#                 cur = string_alt[i] - num_code[i]
#                 nxt.append(cur)
#             self.findpath(nxt, code_dict, path + [num_code])


# a = Solution()
# b = a.originalDigits("zeroonetwothreefourfivesixseveneightnine")
# print(b)
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnts = collections.Counter(s)
        nums = ['six', 'zero', 'two', 'eight', 'seven', 'four', 'five', 'nine', 'one', 'three']
        numc = [collections.Counter(num) for num in nums]
        digits = [6, 0, 2, 8, 7, 4, 5, 9, 1, 3]
        ans = [0] * 10
        for idx, num in enumerate(nums):
            cntn = numc[idx]
            t = min(cnts[c] //  cntn[c] for c in cntn)
            ans[digits[idx]] = t
            for i in range(t):
                cnts.subtract(cntn)
        return ''.join(str(i) * n for i, n in enumerate(ans))
# @lc code=end

