#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k, n):
        if k == 0 or n == 0:
            return []
        self.ans = []
        self.k = k
        self.back(n, 0, [])
        return self.ans       

    def back(self, rest, count, path):
        if rest == 0 and count == self.k:
            self.ans.append(path)
        if rest > (self.k - count) * 9:
            return
        if rest < self.k - count:
            return
        if rest < 0:
            return 
        for i in range(1, 10):
            if not path or (path and i > path[-1]):
                self.back(rest - i, count + 1, path + [i])

if __name__ == '__main__':
    a = Solution()
    b = a.combinationSum3(3, 7)
    print(b)

# @lc code=end

