#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
import collections
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        t = collections.Counter(tasks)
        step = 0
        heap = []
        for k, v in t.items():
            heapq.heappush(heap, (-v, k))
        while heap:
            temp = []
            cnt = 0
            mx_time = min(len(heap), n + 1)
            while cnt < mx_time:
                curtime, curele = heapq.heappop(heap)
                step += 1
                cnt += 1
                if curtime < -1:
                    temp.append((curtime + 1, curele))
            if temp:
                step += n + 1 - mx_time
            for tempitem in temp:
                heapq.heappush(heap, tempitem)
        return step

# if __name__ == '__main__':
#     a = Solution()
#     b = a.leastInterval(["A","A","A","B","B","B"], 2)
#     print(b)
# @lc code=end

