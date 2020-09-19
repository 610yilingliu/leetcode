#
# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#

# @lc code=start
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        res = []
        for x in range(N, 0, -1):
            i = A.index(x)
            if i != 0:
                res.append(i + 1)
            res.append(x)
            self.reverse(A, 0, i + 1);
            self.reverse(A, 0, x);
            print(A)
        return res
    
    #[start, end)
    def reverse(self, A, start, end):
        A[start:end] = A[start:end][::-1]
# @lc code=end

