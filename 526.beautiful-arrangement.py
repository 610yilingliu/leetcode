#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
class Solution:
    def countArrangement(self, N: int):
        if N == 1:
            return 1
        self.ans = 0
        nums = [i for i in range(1, N + 1)]
        self.generator([], nums)
        return self.ans

    def generator(self, path, rest):
        if not rest:
            self.ans += 1
        for i in range(len(rest)):
            if (len(path) + 1) % rest[i] == 0 or rest[i] % (len(path) + 1) == 0:
                self.generator(path + [rest[i]], rest[:i] + rest[i + 1:])

if __name__ == '__main__':
    a = Solution()
    b = a.countArrangement(2)
    print(b)

# @lc code=end

