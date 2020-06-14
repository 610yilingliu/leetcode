#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums, target):
        if nums == []:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        if len(set(nums)) != len(nums):
            return -1
        mid = int((len(nums) - 1)/2) + 1
        for i in range(0, mid):
            if target == nums[i]:
                return i
            if target == nums[len(nums) - 1 - i]:
                return len(nums) - 1 - i
        if nums[mid]:
            if nums[mid] == target:
                return mid
        return  -1
        
if __name__ == '__main__':
    a = Solution()
    b = a.search([4,5,6,7,0,1,2], 0)
    print(b)
# @lc code=end

