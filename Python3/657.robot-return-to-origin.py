#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
import collections

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = collections.Counter(moves)
        return c['U'] == c['D'] and c['L'] == c['R']
        
# @lc code=end

