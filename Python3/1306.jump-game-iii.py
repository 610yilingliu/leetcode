#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited_pos = set()
        def dfs(pos):
            if pos >= len(arr):
                return False
            if pos < 0:
                return False
            if pos in visited_pos:
                return
            if arr[pos] == 0:
                return True
            visited_pos.add(pos)
            left_pos = pos - arr[pos]
            right_pos = pos + arr[pos]
            if dfs(left_pos) or dfs(right_pos):
                return True
            return False
        return dfs(start)
            

# @lc code=end

