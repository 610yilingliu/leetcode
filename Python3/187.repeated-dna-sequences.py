#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) <= 10:
            return []
        repeated = []
        bit_dic = {
            # 00
            'A': 0,
            # 01 
            'C': 1,
            # 10
            'G': 2,
            # 11
            'T': 3
        }
        repeated_dict = dict()
        ans = []
        limit = (1 << 20) - 1
        current_bit = 0
        for i in range(9):
            current_bit = ((current_bit << 2) + bit_dic[s[i]]) & limit
        for i in range(9, len(s)):
            current_bit = ((current_bit << 2) + bit_dic[s[i]]) & limit
            if current_bit not in repeated_dict:
                repeated_dict[current_bit] = 1
            else:
                repeated_dict[current_bit] += 1
                if repeated_dict[current_bit]  == 2:
                    ans.append(s[i - 9: i + 1])
        return ans
# @lc code=end

