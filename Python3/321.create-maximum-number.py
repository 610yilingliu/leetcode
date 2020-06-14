#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#

# @lc code=start
# class Solution:
#     def maxNumber(self, nums1, nums2, k):
#         if not nums1 and not nums2:
#             return []
#         l1, l2 = len(nums1), len(nums2)
#         dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
#         if k >= l1:
#             for i in range(1, l1 + 1):
#                     dp[i][0] = dp[i - 1][0] * 10 + nums1[i - 1]
#         else:
#             for i in range(1, k + 1):
#                 dp[i][0] = dp[i - 1][0] * 10 + nums1[i - 1]
#             for i in range(k + 1, l1 + 1):
#                 curnum = dp[i - 1][0] % 10 * 10 + nums1[i - 1]
#                 dp[i][0] = max(curnum, dp[i - 1][0])
#             if not nums2:
#                 return dp[-1][0]

#         if k >= l2:
#             for j in range(1, l2 + 1):
#                 dp[0][j] = dp[0][j - 1] * 10 + nums2[j - 1]
#         else:
#             for j in range(1, k + 1):
#                 dp[0][j] = dp[0][j - 1] + nums2[j - 1]
#             for i in range(k + 1, l2 + 1):
#                 curnum = dp[0][j - 1] % 10 + nums2[j - 1]
#                 dp[0][j] = max(dp[0][j - 1], curnum)
#             if not nums1:
#                 return dp[0][-1]

#         for i in range(1, l1 + 1):
#             for j in range(1, l2 + 1):
#                 last1 = dp[i - 1][j]
#                 last2 = dp[i][j - 1]
#                 dp[i][j] = max(self.insert(nums1[i - 1], last1, k), self.insert(nums2[j - 1], last2, k))
        
#         number = str(dp[-1][-1])
#         ans = []
#         for digit in number:
#             ans.append(digit)
#         return ans

#     def insert(self, newdigit, orinum, limit):
#         d, num = str(newdigit), str(orinum)
#         mx = float('-inf')
#         if len(num) + 1 <= limit:
#             for i in range(len(num)):
#                 mx = max(int(num[:i] + d + num[i:]), mx)
#             return mx
#         for i in range(len(num)):
#             mx = max(int(num[:i] + d + num[i + 1:]), mx)
#         return mx



class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
 
        def get_max_sub_array(nums, k):
            res , n = [] ,len(nums)
            for i in range(n):
                while res and len(res) + n - i > k and nums[i] > res[-1]:
                    res.pop()
                if len(res) < k:
                    res.append(nums[i])
            return res
 
        ans = [0] * k
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            res1 = get_max_sub_array(nums1, i)
            res2 = get_max_sub_array(nums2, k - i)
            ans = max(ans, [max(res1, res2).pop(0) for _ in range(k)])
        return ans
if __name__ == '__main__':
    a = Solution()
    b = a.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
    print(b)
# @lc code=end

