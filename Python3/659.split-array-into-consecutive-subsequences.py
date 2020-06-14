#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#

# @lc code=start
import collections
import heapq

class Solution:
    def isPossible(self, nums):
        lists = collections.defaultdict(list)
        for num in nums:
            prelens = lists[num - 1]
            if not prelens:
                prelen = 0
            else:
                prelen = heapq.heappop(prelens)
            cur = lists[num]
            heapq.heappush(cur,prelen + 1)
            lists[num] = cur
        for values in lists.values():
            for v in values:
                if v < 3:
                    return False
        return True

        
# if __name__ == '__main__':
#     a = Solution()
#     b = a.isPossible([1,2,3,4,4,5])
#     print(b)

# @lc code=end

