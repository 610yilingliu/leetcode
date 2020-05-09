#
# @lc app=leetcode id=358 lang=python3
#
# [358] Rearrange String k Distance Apart
#
import heapq
import collections
# @lc code=start
class Solution:
    def rearrangeString(self, s, k):
        if k < 1:
            return s
        d = collections.Counter(s)
        rest = len(s)
        heap = []
        for key, val in d.items():
            heapq.heappush(heap, (-val, key))
        ans = ''
        while heap:
            time = min(rest, k)
            pre_round = []
            for i in range(time):
                if not heap:
                    return ''
                pretime, char = heapq.heappop(heap)
                ans += char
                if -pretime > 1:
                    pre_round.append((pretime + 1, char))
                rest -= 1
            for item in pre_round:
                heapq.heappush(heap, item)
        return ans


            
# if __name__ == '__main__':
#     a = Solution()
#     b = a.rearrangeString("a", 0)
#     print(b)


# @lc code=end

