#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
import collections

class Solution:
    def longestConsecutive(self, nums):
        d = {}
        mx = 0
        for num in nums:
            if num not in d:
                left = d.get(num - 1, 0)
                right = d.get(num + 1, 0)
                l = left + right + 1
                mx = max(mx, l)
                for number in [num - left, num, num + right]:
                    d[number] = l
        return mx




if __name__ == '__main__':
    a = Solution()
    b = a.longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])
    print(b)

# @lc code=end

