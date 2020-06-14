#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations):
        citations.sort()
        if not citations or citations[-1] == 0:
            return 0
        mx = len(citations)
        ans = 0
        for idx, c in enumerate(citations):
            ans = max(ans, min(mx - idx, c))
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.hIndex([11, 15])
    print(b)
# @lc code=end

