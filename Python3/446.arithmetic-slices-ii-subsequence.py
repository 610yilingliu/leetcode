#
# @lc app=leetcode id=446 lang=python3
#
# [446] Arithmetic Slices II - Subsequence
#

# @lc code=start
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)
        ans = 0
        dp = [collections.defaultdict(int) for x in range(size)]
        for x in range(size):
            for y in range(x):
                delta = A[x] - A[y]
                dp[x][delta] += 1
                if delta in dp[y]:
                    dp[x][delta] += dp[y][delta]
                    ans += dp[y][delta]
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.numberOfArithmeticSlices([2,4,6,8,10])
    print(b)
# @lc code=end

