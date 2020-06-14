#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums):
        if len(nums) < 2:
            return 0
        self.nums = nums
        return self.helper(0, nums[0], 1)

    def helper(self, cur_pos, cur_max, step):
        nums = self.nums
        if cur_pos + cur_max >= len(nums) - 1:
            return step
        mx = 0
        nxt = 0
        for i in range(cur_pos, cur_pos + cur_max + 1):
            if nums[i] + i > mx:
                mx = nums[i] + i
                nxt = i
        return self.helper(nxt, nums[nxt], step + 1)  

if __name__ == '__main__':
    a = Solution()
    b = a.jump([1,2,3])
    print(b)
# @lc code=end

