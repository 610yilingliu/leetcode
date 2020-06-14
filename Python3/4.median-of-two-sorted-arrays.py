#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not (nums1 == [] and nums2 ==[]):
            midpoint = (len(nums1) + len(nums2))/2
            count = 0
            current = float("-inf")
            temp1 = temp2 = float("inf")
            if midpoint % 1 != 0:
                while count < midpoint:
                    if nums1:
                        temp1 = nums1[0]
                    if nums2:
                        temp2 = nums2[0]
                    if temp1 < temp2:
                        current = temp1
                        temp1 = float("inf")
                        nums1.pop(0)
                    else:
                        current = temp2
                        temp2 = float("inf")
                        nums2.pop(0)
                    count += 1
            else:
                while count <= midpoint:
                    current2 = current
                    if nums1:
                        temp1 = nums1[0]
                    if nums2:
                        temp2 = nums2[0]
                    if temp1 < temp2:
                        current = temp1
                        temp1 = float("inf")
                        nums1.pop(0)
                    else:
                        current = temp2
                        temp2 = float("inf")
                        nums2.pop(0)
                    count += 1    
                current = (current + current2)/2
            return current     
        return 0  
# @lc code=end

