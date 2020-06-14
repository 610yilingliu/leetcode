#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board):
        valid = {'1','2','3','4','5','6','7','8','9','.'}
        # check condition 1 and 2
        for i in range(9):
            # horizontal
            temp_hor = set()
            # vertical
            temp_ver = set()
            for j in range(9):
                # horizontal
                if board[i][j] not in valid:
                    return False
                # if duplicated
                if board[i][j] in temp_hor and board[i][j] != '.':
                    return False
                temp_hor.add(board[i][j])
                # vertical, valid is already checked
                # if duplicated
                if board[j][i] in temp_ver and board[j][i] != '.':
                    return False
                temp_ver.add(board[j][i])
        # check condition 3
        for i in range(1, 9, 3):
            for j in range(1, 9, 3):
                h_min = i - 1
                h_max = i + 1
                v_min = j - 1
                v_max = j + 1
                temp_box = set()
                for a in range(h_min, h_max + 1):
                    for b in range(v_min, v_max + 1):
                        if board[a][b] in temp_box and board[a][b] != '.':
                            return False
                        temp_box.add(board[a][b])
        return True

# @lc code=end

