#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]):
        i = 0
        j = 1
        n = len(nums)-1
        while n>0:
            if nums[i] == nums[j]:
                del nums[i]
            else:
                i+=1
                j+=1
            n-=1

if __name__ == '__main__':
    a = Solution()
    b = a.removeDuplicates([1,1,2])
    print(b)
# @lc code=end

