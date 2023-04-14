#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
class Solution(object):
    
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        if not piles:
            return False
        self.F = [[0 for i in range(len(piles))] for j in range(len(piles))]
        self.S = [[0 for i in range(len(piles))] for j in range(len(piles))]
        _sum = sum(piles)
        alex = self.f(piles, 0, len(piles) - 1)
        return alex > _sum / 2
        
    def f(self, piles, i, j):
        """
        先选
        """
        if i == j:
            return piles[i]
        if self.F[i][j] != 0:
            return self.F[i][j]
        curr = max(piles[i] + self.s(piles, i + 1, j), piles[j] + self.s(piles, i, j - 1))
        self.F[i][j] = curr
        return curr
        
    def s(self, piles, i, j):
        """
        后选
        """
        if i == j:
            return 0
        if self.S[i][j] != 0:
            return self.S[i][j]
        curr = min(self.f(piles, i + 1, j), self.f(piles, i, j - 1))
        self.S[i][j] = curr
        return curr

a = Solution()
b = a.stoneGame([5,3,4,5])
print(b)
# @lc code=end

