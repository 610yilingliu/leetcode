#
# @lc app=leetcode id=6 lang=python3
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        temp = [''] * numRows
        r = 0
        step = 1
        for c in s:
            temp[r] += c
            if r == 0:
                step = 1
            elif r == numRows -1:
                step = -1
            r += step
        final = ''
        for i in range(len(temp)):
            final += temp[i]
        return final

# @lc code=end

if __name__ == '__main__':
    a = Solution()
    b = a.convert("ABC",1)
    print(b)