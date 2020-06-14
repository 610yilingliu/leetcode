#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import collections
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        d = collections.Counter(nums)
        heap = []
        for key, val in d.items():
            heapq.heappush(heap, [-val, key])
        ans = []
        count = 0
        while count < k:
            ans.append(heapq.heappop(heap)[1])
            count += 1
        return ans

# @lc code=end

