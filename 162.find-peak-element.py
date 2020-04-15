#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    # merging sorting
    def findPeakElement(self, nums):
        self.mx = float('-inf')
        self.idx = -1
        self.merge_sort(nums, 0, len(nums))
        return self.idx

    
    def merge_sort(self, ls, start, end):
        if start >= end:
            return
        if end - start == 1:
            if ls[start] > self.mx:
                self.mx = ls[start]
                self.idx = start
            return
        self.merge_sort(ls, start, ((end - start) >> 1) + start)
        self.merge_sort(ls, ((end - start) >> 1) + start, end)

if __name__ == '__main__':
    a = Solution()
    b = a.findPeakElement([1,2,1,3,5,6,4])
    print(b)
# @lc code=end

