#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board, word):
        start = [None, None]
        h = len(board)
        l = len(board[0])
        walked = [[0] * l for _ in range(h)]
        for i in range(h):
             for j in range(l):
                 if board[i][j] == word[0]:
                    start = [i, j]
                    walked[i][j] = 1
                    if self.helper(word[1:], board, walked, start):
                        return True
                    walked[i][j] = 0

        return False
        
    def helper(self, rest, board, walked, current_pos):
        if len(rest) == 0:
            return True
        i = current_pos[0]
        j = current_pos[1]
        if i > 0 and board[i - 1][j] == rest[0] and walked[i - 1][j] == 0:
            walked[i - 1][j] = 1
            if self.helper(rest[1:], board, walked, [i - 1, j]):
                return True
            walked[i - 1][j] = 0
            

        if i < len(board) - 1 and board[i + 1][j] == rest[0] and walked[i + 1][j] == 0:
            walked[i + 1][j] = 1
            if self.helper(rest[1:], board, walked, [i + 1, j]):
                return True
            walked[i + 1][j] = 0

        if j > 0 and board[i][j - 1] == rest[0] and walked[i][j - 1] == 0:
            walked[i][j - 1] = 1
            if self.helper(rest[1:], board, walked, [i, j - 1]):
                return True
            walked[i][j - 1] = 0   

        if j < len(board[0]) - 1 and board[i][j + 1] == rest[0] and walked[i][j + 1] == 0:
            walked[i][j + 1] = 1
            if self.helper(rest[1:], board, walked, [i, j + 1]):
                return True
            walked[i][j + 1] = 0
        return False

# @lc code=end

