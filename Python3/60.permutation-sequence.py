#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
import heapq

class Solution:
    def getPermutation(self, n, k):
        if n < 2:
            return str(n)
        if k == 1:
            ans = ''
            for i in range(1, n + 1):
                ans += str(i)
            return ans
        nums = [num for num in range(1, n + 1)]
        dividers = [1] * (n)
        for i in range(1, n):
            dividers[i] = i * dividers[i - 1]
        ans = ""
        n = n - 1
        k = k - 1
        while nums:
            cur_div = dividers[n]
            curidx = k // cur_div
            k = k % cur_div
            ans += str(nums[curidx])
            nums.pop(curidx)
            n -= 1
        return ans
        

if __name__ == '__main__':
    a = Solution()
    b = a.getPermutation(4, 9)
    print(b)



# @lc code=end

