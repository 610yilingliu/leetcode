#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#

# @lc code=start
class Solution:
    def countBattleships(self, board):
        if not board or not board[0]:
            return 0
        ans = 0
        x_mx = len(board[0])
        y_mx = len(board)
        for i in range(y_mx):
            for j in range(x_mx):
                if board[i][j] == 'X':
                    ans += 1
                    self.finder(board, i, j, y_mx, x_mx)
        return ans

    def finder(self, board, cury, curx, ymx, xmx):
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        if board[cury][curx] == 'X':
            board[cury][curx] = '.'
            for d in directions:
                new_y = cury + d[0]
                new_x = curx + d[1]
                if 0 <= new_y < ymx and 0 <= new_x < xmx:
                    self.finder(board, new_y, new_x, ymx, xmx)
            
# a = Solution()
# b = a.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
# @lc code=end

