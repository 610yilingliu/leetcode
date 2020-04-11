#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, A):
        if len(A) == 1:
            return True
        pre = 1
        for i in range(1, len(A)):
            if A[i] - A[i - 1] != 0 and pre == 1:
                pre = (A[i] - A[i - 1]) >> 32
            if pre!= 1 and A[i]!= A[i - 1] and (A[i] - A[i - 1]) >> 32 != pre:
                return False
        return True
        
if __name__ == '__main__':
    a = Solution()
    b = a.isMonotonic([6,5,4,4])
    print(b)

# @lc code=end

