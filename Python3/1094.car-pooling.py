#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
import heapq
class Solution:
    def carPooling(self, trips, capacity):
        if not trips or not trips[0]:
            return False
        trips = sorted(trips, key = lambda trip: (trip[1], trip[2]))
        unload_ls = []
        for trip in trips:
            while unload_ls and unload_ls[0][0] <= trip[1]:
                capacity += unload_ls[0][1]
                heapq.heappop(unload_ls)
            capacity -= trip[0]
            if capacity < 0:
                return False
            heapq.heappush(unload_ls, (trip[2], trip[0]))
        return True

a = Solution()
b = a.carPooling([[10,5,7],[10,3,4],[7,1,8],[6,3,4]], 24)
print(b)
# @lc code=end

