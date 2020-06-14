#
# @lc app=leetcode id=254 lang=python3
#
# [254] Factor Combinations
#

# @lc code=start
class Solution:
    def getFactors(self, n: int):
        self.ans = []
        self.helper(n,[])
        return self.ans

    def helper(self, n, path):
        if not path:
            divider = 2
        else:
            divider = path[-1]
        while divider <= n/divider:
            if n % divider == 0:
                path.append(divider)
                path.append(n // divider)
                self.ans.append(path.copy())
                path.pop()
                self.helper(n//divider, path)
                path.pop()
            divider += 1



if __name__ == '__main__':
    a = Solution()
    b = a.getFactors(12)
    print(b)




# @lc code=end

