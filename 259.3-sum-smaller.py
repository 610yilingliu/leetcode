#
# @lc app=leetcode id=259 lang=python3
#
# [259] 3Sum Smaller
#

# @lc code=start
class Solution:
    def threeSumSmaller(self, nums, target):
        if not nums or len(nums) < 3:
            return 0
        if nums[0] + nums[1] + nums[2] > target:
            return 0
        nums.sort()
        mx = len(nums)
        ans = 0
        for l in range(0, mx - 2):
            if nums[l] + nums[l + 1] + nums[l + 2] >= target:
                break
            if nums[l] + nums[mx - 2] + nums[mx - 1] < target:
                ans += (mx - 1 - l) * (mx - 2 - l) // 2
                continue
            m = l + 1
            r = mx - 1
            while m < r:
                tmp = nums[l] + nums[m] + nums[r]
                if tmp < target:
                    ans += r - m
                    m += 1
                if tmp >= target:
                    r -= 1
        return ans

# if __name__ == '__main__':
#     a = Solution()
#     b = a.threeSumSmaller([2,0,0,2,-2], 2)
#     print(b)
# @lc code=end

