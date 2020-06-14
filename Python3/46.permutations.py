#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums):
        if nums == []:
            return []
        ans = [[]]
        for _ in range(len(nums)):
            temp = []
            for item in ans: 
                for ele in nums:
                    if ele not in item:
                        temp.append([ele] + item)
                ans = temp
        return ans


# @lc code=end

