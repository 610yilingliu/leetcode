#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates, target):
        if candidates == []:
            return []
        candidates.sort()
        self.ans = []
        self.helper(candidates, 0, target, [])
        return self.ans

    def helper(self, candidates, start, re, ls):
        if re == 0 and ls not in self.ans:
            self.ans.append(ls)
        if re < 0:
            return
        for i in range(start, len(candidates)):
            if re < candidates[i]:
                return
            start = start + 1
            self.helper(candidates, start, re - candidates[i], ls + [candidates[i]])



if __name__ == '__main__':
    a = Solution()
    b = a.combinationSum2([10,1,2,7,6,1,5], 8)
    print(b)
# @lc code=end

