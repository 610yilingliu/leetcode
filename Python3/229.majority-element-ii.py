#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
import collections

# @lc code=start
class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        mi = len(nums)/3
        d = collections.defaultdict(int)
        ans = []
        for item in nums:
            if d[item] <= mi:
                d[item] += 1
            if item not in ans and d[item] > mi:
                ans.append(item)
        return ans



        
# @lc code=end

if __name__ == '__main__':
    a = Solution
    b = a.majorityElement([3,2,3])
    print(b)
