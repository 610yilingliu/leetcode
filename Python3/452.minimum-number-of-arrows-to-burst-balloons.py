#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points):
        if len(points) < 2:
            return len(points)
        points.sort()
        ans = 1
        start = points[0][0]
        end = points[0][1]
        for i in range(1, len(points)):
            if start == points[i][0]:
                continue
            if end >= points[i][0]:
                start = points[i][0]
                if end > points[i][1]:
                    end = points[i][1]
            else:
                ans += 1
                start = points[i][0]
                end = points[i][1]
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]])
    print(b)

        
# @lc code=end

