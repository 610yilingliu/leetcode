#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        heights.append(0)
        stack = []
        mx = 0
        for i in range(len(heights)):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack.pop()]
                    if not stack:
                        l = i
                    else:
                        l = i - stack[-1] - 1
                    mx = max(mx, h * l)
                stack.append(i)
        return mx


if __name__ == '__main__':
    a = Solution()
    b = a.largestRectangleArea([1])
    print(b)
                    

            
        
# @lc code=end

