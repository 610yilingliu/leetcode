#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        l = len(nums)
        if l < 3:
            return []
        sol = []
        nums.sort()
        for i in range(l - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[l - 1] + nums[l - 2] < 0:
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            mid = i + 1
            right = l - 1
            while mid < right:
                tmp = nums[i] + nums[mid] + nums[right]
                if tmp == 0:
                    sol.append([nums[i], nums[mid], nums[right]])
                    while mid + 1 < right and nums[mid] == nums[mid + 1]:
                        mid = mid + 1
                    mid = mid + 1
                    while mid < right - 1 and nums[right] == nums[right - 1]:
                        right = right - 1
                    right = right - 1
                elif tmp > 0:
                    right = right -1
                else:
                    mid = mid + 1
        return sol


                

if __name__ == '__main__':
    a = Solution()
    b = a.threeSum([-1,0,1,2,-1,-4])
    print(b)
# @lc code=end

