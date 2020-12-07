#
# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        curzero = 0
        lp = 0
        rp = 0
        mxlen = 0
        while rp < len(nums):
            if nums[rp] == 0:
                curzero += 1
                if curzero > 1:
                    mxlen = max(mxlen, rp - lp)
                    while curzero > 1:
                        if nums[lp] == 0:
                            curzero -= 1
                        lp += 1
            rp += 1
        mxlen = max(mxlen, rp - lp)
        return mxlen

a = Solution()
b = a.findMaxConsecutiveOnes([1,0,1,1,0,1])
print(b)
# @lc code=end

