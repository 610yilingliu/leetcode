#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

# @lc code=start
class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        if rooms and rooms[0]:
            x_mx = len(rooms[0])
            y_mx = len(rooms)
            directions  = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            def replacement(y, x, curstep):
                for d in directions:
                    new_x = x + d[0]
                    new_y = y + d[1]
                    if 0 <= new_x < x_mx and 0 <= new_y < y_mx:
                        if rooms[new_y][new_x] > 0:
                            if curstep < rooms[new_y][new_x]:
                                rooms[new_y][new_x] = curstep
                                replacement(new_y, new_x, curstep + 1)

            for i in range(y_mx):
                for j in range(x_mx):
                    if rooms[i][j] == 0:
                        replacement(i, j, 1)

# @lc code=end

