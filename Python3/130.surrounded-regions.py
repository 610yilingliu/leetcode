#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return
        self.ignored = []
        h = len(board)
        l = len(board[0])
        for i in range(l):
            if board[0][i] == 'O':
                self.ignored.append([0, i])
            if board[-1][i] == 'O':
                self.ignored.append([h - 1, i])
        for j in range(1, h - 1):
            if board[j][0] == 'O':
                self.ignored.append([j, 0])
            if board[j][-1] =='O':
                self.ignored.append([j, l - 1])
        for item in self.ignored:
            self.appender(item, board)
        for i in range(h):
            for j in range(l):
                if [i,j] not in self.ignored and board[i][j] == 'O':
                    board[i][j] = 'X'


    def appender(self, current_pos, matrix):
        y = current_pos[0]
        x = current_pos[1]
        if y > 0:
            if matrix[y - 1][x] == 'O':
                if [y - 1, x] not in self.ignored:
                    self.ignored.append([y - 1, x])
                    self.appender([y - 1, x], matrix)

        if y < len(matrix) - 1:
            if matrix[y + 1][x] == 'O':
                if [y + 1, x] not in self.ignored:
                    self.ignored.append([y + 1, x])
                    self.appender([y + 1, x], matrix)
        if x > 0:
            if matrix[y][x - 1] == 'O':
                if [y, x - 1] not in self.ignored:
                    self.ignored.append([y, x - 1])
                    self.appender([y, x - 1], matrix)

        if x < len(matrix[0]) - 1:
            if matrix[y][x + 1] == 'O':
                if [y, x + 1] not in self.ignored:
                    self.ignored.append([y, x + 1])
                    self.appender([y, x + 1], matrix) 
        


# @lc code=end

