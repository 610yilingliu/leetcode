#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        dq = collections.deque()
        n = len(nums)
        ans = []

        for i in range(k-1):
            while len(dq) > 0:
                if nums[dq[-1]] <= nums[i]:
                    dq.pop()
                else:
                    break
            dq.append(i)  

        for i in range(k-1, n):
            while len(dq) > 0:
                if nums[dq[-1]] <= nums[i]:
                    dq.pop()
                else:
                    break
            dq.append(i)

            while dq[0] < i-k+1:
                dq.popleft()
            ans.append(nums[dq[0]])

        return ans

a = Solution()
b = a.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print(b)


# @lc code=end

