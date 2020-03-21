#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates, target):
        if len(candidates) == 0:
            return []
        candidates.sort()
        self.ans = []
        self.helper(candidates, [], target, 0)
        return self.ans
        
    def helper(self, candidates, ls, remain, last_num):
        if remain == 0 :
            self.ans.append(ls)
        if remain < candidates[0]:
            return
        for item in candidates:
            if item > remain:
                return
            if item < last_num:
                continue
            self.helper(candidates, ls + [item], remain - item, item)
            
if __name__ == '__main__':
    a = Solution()
    b = a.combinationSum([10,1,2,7,6,1,5], 8)
    print(b)
# @lc code=end

