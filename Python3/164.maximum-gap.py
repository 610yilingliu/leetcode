#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
import collections

class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return abs(nums[1] - nums[0])
        mx = max(nums)
        mi = min(nums)
        rg = max(1, (mx - mi)//len(nums))
        containers = [collections.deque() for _ in range((mx - mi)//rg + 1)]
        
        for num in nums:
            cur = (num - mi)//rg
            if len(containers[cur]) == 0:
                containers[cur].append(num)
                containers[cur].append(num)
            elif num > containers[(num - mi)//rg][1]:
                containers[cur][1] = num
            elif num < containers[(num - mi)//rg][0]:
                containers[cur][0] = num
        ans = 0
        pre = None
        i = 0
        while i < len(containers):
            while i < len(containers) and len(containers[i]) < 1:
                i += 1
            if pre is None:
                pre = containers[i][1]
            else:
                ans = max(ans, containers[i][0] - pre)
                pre = containers[i][1]
            i += 1
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.maximumGap([1,1,1,1,1,5,5,5,5,5])
    print(b)
# @lc code=end

