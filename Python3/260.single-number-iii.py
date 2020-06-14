#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums):
        temp_res = 0
        for num in nums:
            temp_res ^= num
        # temp_res = ans1 ^ ans2
        bit_pos = 0
        while temp_res & 1 == 0:
            bit_pos += 1
            temp_res >>= 1
        anchor = 1 << bit_pos
        a = 0
        b = 0
        for num in nums:
            if num & anchor == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]

if __name__ == '__main__':
    a = Solution()
    b = a.singleNumber([1,2,1,3,2,5])
    print(b)
# @lc code=end

