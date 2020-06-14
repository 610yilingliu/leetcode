#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums):
        storage = set()
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == nums[j]:
                return nums[i]
            if nums[i] in storage:
                return nums[i]
            if nums[j] in storage:
                return nums[j]
            storage.add(nums[i])
            storage.add(nums[j])
            i += 1
            j -= 1
        # if length is an odd number, like [3,1,3,4,2]
        if j == i:
            mid = len(nums)//2
            if nums[mid] in storage:
                return nums[mid]
        return None


if __name__ == '__main__':
    a = Solution()
    b = a.findDuplicate([3,1,3,4,2])
    print(b)

# @lc code=end

