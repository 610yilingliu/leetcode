#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        len1, len2 = len(nums1), len(nums2)
        if not len1 or not len2: return res
        heap = []
        for x in range(len1):
            heapq.heappush(heap, (nums1[x] + nums2[0], x, 0))
        while len(res) < min(k, len1 * len2):
            s, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len2:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res

if __name__ == '__main__':
    a = Solution()
    b = a.kSmallestPairs(nums1 =[1,2,3] , nums2 = [1,1,1,5], k = 6)
    print(b)

        
# @lc code=end

