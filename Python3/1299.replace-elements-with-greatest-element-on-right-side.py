#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        max_idxs = []
        def helper(idx):
            mx = float('-inf')
            ridx = -1
            for i in range(idx + 1, len(arr)):
                if arr[i] > mx:
                    mx = arr[i]
                    ridx = i
            return mx, ridx

        for i in range(len(arr)):
            if i - 1 > 0 and max_idxs[i - 1] > i:
                res.append(res[-1])
                max_idxs.append(max_idxs[-1])
            else:
                mx, ix = helper(i)
                res.append(mx if ix != -1 else -1)
                max_idxs.append(ix)
        return res
            
# @lc code=end

