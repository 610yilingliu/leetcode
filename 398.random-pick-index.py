#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#

# @lc code=start
import collections
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.d = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            self.d[num].append(idx)

    def pick(self, target: int):
        if target in self.d:
            ans_ls = self.d[target]
            place = random.randint(0, len(ans_ls) - 1)
            return ans_ls[place]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

