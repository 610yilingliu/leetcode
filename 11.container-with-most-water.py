#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        maximun = 0
        while l < r:
            h = min(height[l], height[r])
            b = r - l
            maximun = max(maximun, h * b)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maximun



if __name__ == '__main__':
    a = Solution()
    b = a.maxArea([1,8,6,2,5,4,8,3,7])
    print(b)

# @lc code=end

