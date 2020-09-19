#
# @lc app=leetcode id=1103 lang=python3
#
# [1103] Distribute Candies to People
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies, num_people):
        curcandy = 0
        curpos = -1
        ans = [0] * num_people
        while candies > 0:
            if curpos == num_people - 1:
                curpos = 0
            else:
                curpos += 1
            curcandy += 1
            if candies < curcandy:
                ans[curpos] += candies
                candies = 0
                break
            else:
                candies -= curcandy
                ans[curpos] += curcandy
        return ans

a = Solution()
b = a.distributeCandies(10, 3)
print(b)
 # @lc code=end

