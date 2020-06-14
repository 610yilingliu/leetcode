#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
# notice: library is faster if you can use it.
# import itertools, collections
# https://leetcode.com/problems/brick-wall/discuss/269086/Python-1-liner-beats-90

class Solution:
    def leastBricks(self, wall):
        # if no wall, return
        if not wall or not wall[0]:
            return 0

        # if only one wall, go through this wall and return
        if len(wall) == 1:
            if len(wall[0]) == 1:
                return 1
            return 0

        if max([len(row) for row in wall]) == 1:
            return len(wall)

        through_dic= dict()
        for i in range(len(wall)):
            s  = 0
            for j in range(len(wall[i]) - 1):
                s += wall[i][j]
                # equal to if s not in d: d[s] = 1;else d[s] += 1
                through_dic[s] = through_dic.get(s, 0) + 1
        max_same = max([val for key, val in through_dic.items()])
        return len(wall) - max_same

if __name__ == '__main__':
    a = Solution()
    b = a.leastBricks([[1]])
    print(b)

# @lc code=end

