#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
import collections
import heapq
# @lc code=start
class Solution:
    def reorganizeString(self, S):
        d = collections.Counter(S)
        ans = ''
        heap = []
        rest = len(S)
        for k, v in d.items():
            heapq.heappush(heap, (-v, k))
        while heap:
            time = min(rest, 2)
            pre = []
            for i in range(time):
                if not heap:
                    return ''
                pretime, char = heapq.heappop(heap)
                ans += char
                if -pretime > 1:
                    heapq.heappush(pre, (pretime + 1, char))
                rest -= 1
            for item in pre:
                heapq.heappush(heap, item)
        return ans


        
        



# @lc code=end

