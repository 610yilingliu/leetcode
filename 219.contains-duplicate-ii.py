#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        d = dict()
        for i in range(len(nums)):    
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                if i - d[nums[i]] <= k:
                    return True
                d[nums[i]] = i
        return False

if __name__ == '__main__':
    a = Solution()
    b = a.containsNearbyDuplicate([1,2,3,1], 3)
    print(b)
# @lc code=end

