#
# @lc app=leetcode id=348 lang=python3
#
# [348] Design Tic-Tac-Toe
#

# @lc code=start
import collections
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.invalid_1 = set()
        self.invalid_2 = set()
        self.p1 = collections.defaultdict(int)
        self.p2 = collections.defaultdict(int)
        self.tar = n
        self.walked = set()


    def move(self, row: int, col: int, player: int):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        def addup(dict_name, invalid_set, another_invalid, locx, locy):
            if locx == locy:
                diag_name = (1,1)
                if diag_name not in invalid_set:
                    dict_name[diag_name] += 1
                    if dict_name[diag_name] == self.tar:
                        return player
                    another_invalid.add(diag_name)
            if locx == self.tar-1-locy:
                diag_name = (-1, -1)
                if diag_name not in invalid_set:
                    dict_name[diag_name] += 1
                    if dict_name[diag_name] == self.tar:
                        return player
                    another_invalid.add(diag_name)
            curcol = (locy, None)
            currow = (None, locx)
            if curcol not in invalid_set:
                dict_name[curcol] += 1
                if dict_name[curcol] == self.tar:
                    return player
                another_invalid.add(curcol)
            if currow not in invalid_set:
                dict_name[currow] += 1
                if dict_name[currow] == self.tar:
                    return player
                another_invalid.add(currow)
            return 0
        res = 0
        if (row, col) not in self.walked:
            if player == 1:
                res = addup(self.p1, self.invalid_1, self.invalid_2, row, col)
            if player == 2:
                res = addup(self.p2, self.invalid_2, self.invalid_1, row, col)
            self.walked.add((row, col))
        return res
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(3)
# ls = [[1,1,2],[0,2,2],[2,0,2]]
# for step in ls:
#     curstate = obj.move(step[0], step[1], step[2])
#     print(curstate)

# @lc code=end

