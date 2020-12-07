#
# @lc app=leetcode id=562 lang=python3
#
# [562] Longest Line of Consecutive One in Matrix
#

# @lc code=start

# 0 -1 matrix, so only 0 and 1 in that matrix
# string '0' or int 0?
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        h, w = len(M), len(M) and len(M[0]) or 0
        ans = 0

        #horizontal & diagonal
        diag = [[0] * w for r in range(h)]
        for x in range(h):
            cnt = 0
            for y in range(w):
                cnt = M[x][y] * (cnt + 1)
                diag[x][y] = M[x][y]
                if x > 0 and y > 0 and M[x][y] and diag[x - 1][y - 1]:
                    diag[x][y] += diag[x - 1][y - 1]
                ans = max(ans, cnt, diag[x][y])

        #vertical & anti-diagonal
        adiag = [[0] * w for r in range(h)]
        for x in range(w):
            cnt = 0
            for y in range(h):
                cnt = M[y][x] * (cnt + 1)
                adiag[y][x] = M[y][x]
                if y < h - 1 and x > 0 and M[y][x] and adiag[y + 1][x - 1]:
                    adiag[y][x] += adiag[y + 1][x - 1]
                ans = max(ans, cnt, adiag[y][x])

        return ans
# @lc code=end

