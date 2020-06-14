#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        mx = 0
        helper = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                curnum = int(matrix[y][x])
                if curnum == 1:
                    cur_width = helper[y][x] = helper[y][x - 1] + 1 if x else 1
                    for i in range(y, -1, -1):
                        cur_width = min(helper[i][x], cur_width)
                        mx = max(mx, cur_width * (y - i + 1))
        return mx

if __name__ == '__main__':
    a = Solution()
    b = a.maximalRectangle([["1"]])
    print(b)
# @lc code=end

