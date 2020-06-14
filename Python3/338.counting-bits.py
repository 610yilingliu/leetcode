#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, num):
        ans = [0]
        if num == 0:
            return ans
        for ones in range(1, num + 1):
            if ones & 1 == 0:
                ans.append(ans[ones >> 1])
            else:
                ans.append(ans[ones >> 1] + 1)
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.countBits(5)
    print(b)
# @lc code=end

