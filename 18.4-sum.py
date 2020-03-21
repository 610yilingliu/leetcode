#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums, target):
        length = len(nums)
        if length < 4:
            return []
        nums.sort()
        result = []
        # ll: left most, l: medium left, r: medium right, rr: right most
        for ll in range(length - 3):
            if nums[ll] + nums[ll + 1] + nums[ll + 2] + nums[ll + 3] > target:
                break
            elif ll > 0 and nums[ll] == nums[ll - 1]: 
                continue
            elif nums[ll] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for l in range(ll + 1, length - 2):
                if l > ll + 1 and nums[l] == nums[l - 1]:
                    continue
                r = l + 1
                rr = length - 1
                while r < rr:
                    s = nums[ll] + nums[l] + nums[r] + nums[rr]
                    if s == target:
                        result.append([nums[ll], nums[l], nums[r], nums[rr]])
                        while r + 1 < rr and nums[r] == nums[r + 1]:
                            r += 1
                        r += 1
                        while r < rr - 1 and nums[rr] == nums[rr - 1]:
                            rr -= 1
                        rr -= 1
                    elif s < target:
                        r += 1
                    else:
                        rr -= 1
        return result

# @lc code=end

