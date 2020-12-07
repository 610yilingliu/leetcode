#
# @lc app=leetcode id=985 lang=python3
#
# [985] Sum of Even Numbers After Queries
#

# @lc code=start
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        count = None
        for val,inx in queries:
            before = A[inx]
            A[inx] += val
            after = A[inx]
            if count == None:
                count = sum(filter(lambda x: x % 2 == 0,A))
            else:
                if before % 2 == 0:
                    count -= before
                if after % 2 == 0:
                    count += after
            res.append(count)
        return res
# @lc code=end

