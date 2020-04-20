#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int):
        self.ans = 0
        board = [-1 for _ in range(n)]
        self.bfs(0, n, board)
        return self.ans

    def checker(self, layer, idx, board):
        for i in range(layer):
            if board[i] == idx or abs(board[i] - idx) == abs(layer - i):
                return False
        return True

    def bfs(self, layer, n, board):
        if layer == n:
            self.ans += 1
        else:
            for i in range(n):
                if self.checker(layer, i, board):
                    board[layer] = i
                    self.bfs(layer + 1, n, board)

if __name__ == '__main__':
    a = Solution()
    b = a.totalNQueens(4)
    print(b)
# @lc code=end

