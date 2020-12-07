#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#

# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        occupied_cnt = 0
        max_distance = 0
        lmost = None
        rmost = None
        last_occupied = None
        for idx, val in enumerate(seats):
            if val == 1:
                occupied_cnt += 1
                if lmost != None:
                    max_distance = max(max_distance, idx - last_occupied)
                else:
                    lmost = idx
                last_occupied = idx
                rmost = idx
        if lmost != rmost:
            return max(max_distance >> 1, lmost, len(seats) - 1 - rmost)
        return max(lmost, len(seats) - 1 - rmost)

# class Solution:
#     def maxDistToClosest(self, seats: List[int]) -> int:
#         seats.append(1)
#         js = -1
#         jss = 0
#         for i, item in enumerate(seats):
#             if item == 1:
#                 if jss == 0 or i == len(seats) - 1:
#                     if (i - js)*2 - 1 >= jss:
#                         jss = (i - js)*2 - 1
#                 else:
#                     if (i - js) >= jss:
#                         jss = (i - js)
#                 js = i
#         return jss // 2
# @lc code=end

