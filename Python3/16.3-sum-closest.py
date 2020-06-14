#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums, target):
        length = len(nums)
        if length < 4:
            return sum(nums)
        nums.sort()
        closet_abs = float('inf')
        res = float('inf')
        for l in range(length - 2):
            # skip if too large
            if nums[l] + nums[l + 1] + nums[l + 2] > target + closet_abs:
                break
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            m = l + 1
            r = length - 1
            while m < r:
                s = nums[l] + nums[m] + nums[r]
                if s == target:
                    return target
                if abs(s - target) < closet_abs:
                    closet_abs = abs(s - target)
                    res = s
                elif s < target:
                    m += 1
                else:
                    r -= 1
        return res

if __name__ == '__main__':
    a = Solution()
    b = a.threeSumClosest([-1, 2, 1, -4], 1)
    print(b)
# @lc code=end

