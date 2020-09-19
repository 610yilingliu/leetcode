#
# @lc app=leetcode id=484 lang=python3
#
# [484] Find Permutation
#

# @lc code=start
class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        size = len(s)
        nums = list(range(1, size + 2))
        ans = []
        idx = 0
        while idx < size:
            if s[idx] == 'D':
                cnt = 0
                while idx < size and s[idx] != 'I':
                    idx += 1
                    cnt += 1
                ans += nums[:cnt+1][::-1]
                nums = nums[cnt+1:]
                if idx < size:
                    idx += 1
            else:
                ans += [nums[0]]
                nums = nums[1:]
                idx += 1
        return ans + nums

a = Solution()
b = a.findPermutation("DDIIDI")
print(b)
# @lc code=end

