#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int):
        if n < 3:
            return 0
        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                prime[i * i : n : i] = [False] * len(prime[i * i : n : i])
        return sum(prime)

if __name__ == '__main__':
    a = Solution()
    b = a.countPrimes(13)
    print(b)
# @lc code=end

