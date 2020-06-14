#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:
    def toHex(self, num: int):
        if num == 0:
            return '0'
        if num < 0:
            num = (1 << 32) + num
        hx = [str(i) for i in range(0, 10)] + ['a', 'b', 'c', 'd', 'e', 'f']
        ans = ''
        while num > 0:
            curnum = 0
            for time in range(0, 4):
                if num == 0:
                    break
                curnum = curnum + ((num & 1) << time)
                num = num >> 1
            ans = hx[curnum] + ans
        return ans

# if __name__ == '__main__':
#     a = Solution()
#     b = a.toHex(-2)
#     print(b)

# @lc code=end

