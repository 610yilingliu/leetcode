#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            nums = nums
        elif len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
        else:
            a = None
            b = None
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] > nums[i - 1]:
                    a = i - 1
                    break
            # if totally reversed
            if a == None:
                cur = int((len(nums) - 1)/2) + 1
                for i in range(0, cur):
                    nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]
            else:
                for i in range(len(nums) - 1, 0, -1):
                    if nums[i] > nums[a]:
                        b = i
                        break

                nums[b], nums[a] = nums[a], nums[b]
                cur = int((a + len(nums) - 1)/2) + 1
                for i in range(a + 1, cur):
                    cur2 = len(nums)-i+a
                    nums[i], nums[cur2] = nums[cur2], nums[i]
                    
if __name__ == '__main__':
    a = Solution()
    b = a.nextPermutation([3,2,1])
    print(b)
        
# @lc code=end

