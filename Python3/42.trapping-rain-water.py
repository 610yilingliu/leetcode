#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
        vol = 0
        l = len(height)
        left = l * [0]
        right = l * [0]

        left[0] = height[0]
        for i in range(1, l):
            left[i] = max(height[i], left[i - 1])

        right[l-1] = height[l - 1]
        for i in range(l -2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        for i in range(1, l-1):
            vol += min(left[i], right[i]) - height[i]
        return vol

# @lc code=end

