#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
import collections
# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        if t == 0:
            # if no duplicated number
            if len(set(nums)) == len(nums):
                return False
            # else check index
            else:
                tempd = dict()
                for idx, num in enumerate(nums):
                    if num not in tempd:
                        tempd[num] = idx
                    else:
                        if idx - tempd[num] <= k:
                            return True
                        tempd[num] = idx
                return False
        # if not equal to zero, do bucket sort
        bucket = collections.OrderedDict()
        b_size = t + 1
        for num in nums:
            key = num//b_size
            if key in bucket:
                return True
            bucket[key] = num
            if key - 1 in bucket and num - bucket[key - 1] <= t:
                return True
            if key + 1 in bucket and bucket[key + 1] - num <= t:
                return True
            # remove the first added key
            if len(bucket) > k:
                bucket.popitem(last = False)
        return False

if __name__ == '__main__':
    a = Solution()
    b = a.containsNearbyAlmostDuplicate([1,2,3,4,5,1], 5, 0)
    print(b)
# @lc code=end

