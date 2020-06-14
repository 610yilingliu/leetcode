#
# @lc app=leetcode id=794 lang=python3
#
# [794] Valid Tic-Tac-Toe State
#

# @lc code=start
class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        xCount, oCount = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'O':
                    oCount += 1
                elif board[i][j] == 'X':
                    xCount += 1
        if oCount != xCount and oCount != xCount - 1: return False
        if oCount != xCount and self.win(board, 'O'): return False
        if oCount != xCount - 1 and self.win(board, 'X'): return False
        return True
        
    def win(self, board, P):
        # board is list[str]
        # P is 'X' or 'O' for two players
        for j in range(3):
            if all(board[i][j] == P for i in range(3)): return True
            if all(board[j][i] == P for i in range(3)): return True
        if board[0][0] == board[1][1] == board[2][2] == P: return True
        if board[0][2] == board[1][1] == board[2][0] == P: return True
        return False



# @lc code=end

