#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
import collections

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        if src == dst:
            return 0
        if not flights:
            return -1
        self.parents = collections.defaultdict(list)
        self.prices = dict()
        for flight in flights:
            self.parents[flight[1]].append(flight[0])
            self.prices[(flight[1], flight[0])] = flight[2]
        self.min_price = float('inf')
        self.searcher(dst, 0, 0, src, dst, K)
        if self.min_price == float('inf'):
            return -1
        return self.min_price

    def searcher(self, curcity, curprice, curstep, src, dst, K):
        if curprice > self.min_price:
            return
        if curcity == src:
            self.min_price = min(self.min_price, curprice)
            return
        if curstep > K:
            return
        if curcity in self.parents:
            par_list = self.parents[curcity]
            for precity in par_list:
                self.searcher(precity, curprice + self.prices[(curcity, precity)], curstep + 1, src, dst, K)

# if __name__ == '__main__':
#     a = Solution()
#     b = a.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
#     print(b)
# @lc code=end

