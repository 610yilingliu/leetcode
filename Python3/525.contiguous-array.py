#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums):
        if not nums or len(nums) < 2:
            return 0
        s = 0
        # start from sum = 0
        d = {0: [-1, -1]}
        for i in range(len(nums)):
            if nums[i] == 0:
                s -= 1
            else:
                s += 1
            if s not in d:
                d[s] = [i, i]
            else:
                d[s] = [d[s][0], i]
        ans = max([d[key][1] - d[key][0] for key in d])
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.findMaxLength([0,1])
    print(b)



# @lc code=end

