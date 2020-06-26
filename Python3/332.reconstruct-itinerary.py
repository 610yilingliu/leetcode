#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
import collections

class Solution:
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        city_counter = len(tickets) + 1
        for pair in tickets:
            graph[pair[0]].append(pair[1])
        for k, v in graph.items():
            v.sort(reverse = True)
        res = []
        self.dfs(graph, "JFK", res)
        return res[::-1]
        
    def dfs(self, graph, frm, res):
        while graph[frm]:
            nxt = graph[frm].pop()
            self.dfs(graph, nxt, res)
        res.append(frm)

# @lc code=end
if __name__ == '__main__':
    a = Solution()
    b = a.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
    print(b)
