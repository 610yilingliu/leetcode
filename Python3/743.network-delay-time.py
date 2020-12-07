#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
import collections

class Solution:
    def networkDelayTime(self, times, N, K):
        path = collections.defaultdict(list)
        for pair in times:
            path[pair[0]].append((pair[1], pair[2]))
        dists = collections.defaultdict(int)
        dists[K] = 0
        queue = collections.deque()
        max_l = 0
        for conn in path[K]:
            queue.append(conn)
            dists[conn[0]] = conn[1]
        while queue:
            cur = queue.popleft()
            curstart = cur[0]
            curd = cur[1]
            for conn in path[curstart]:
                dist_toconn = conn[1] + curd
                if conn[0] not in dists or dist_toconn < dists[conn[0]]:
                    dists[conn[0]] = dist_toconn
                    queue.append((conn[0], dist_toconn))
        shortest_dis = [val for (key, val) in dists.items()]
        if len(shortest_dis) < N:
            return -1
        else:
            shortest_dis.sort()
            return shortest_dis[-1]

a = Solution()
b = a.networkDelayTime([[1,2,1],[2,1,3]], 2, 2)
# @lc code=end

