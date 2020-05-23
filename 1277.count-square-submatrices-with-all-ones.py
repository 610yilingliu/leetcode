#
# @lc app=leetcode id=1277 lang=python3
#
# [1277] Count Square Submatrices with All Ones
#

# @lc code=start
class Solution:
    def countSquares(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        self.mx = min(len(matrix), len(matrix[0]))
        self.ans = 0
        self.counter(matrix, 0)
        return self.ans
        
    
    def counter(self, prematrix, time):
        if time >= self.mx:
            return
        h = len(prematrix)
        l = len(prematrix[0])
        curmatrix = [[0] * (l - 1) for _ in range(h - 1)]

        for i in range(h):
            for j in range(l):
                if prematrix[i][j] == 1:
                    self.ans += 1
                    if i < h - 1 and j < l - 1:
                        if prematrix[i + 1][j] and prematrix[i][j + 1] and prematrix[i + 1][j + 1]:
                            curmatrix[i][j] = 1
        self.counter(curmatrix, time + 1)
                
# @lc code=end

if __name__ == '__main__':
    a = Solution()
    b = a.countSquares([[1,0,1,1,0],[1,1,1,1,1]])
    print(b)
