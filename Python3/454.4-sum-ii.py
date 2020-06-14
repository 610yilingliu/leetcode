#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(self, A, B, C, D):
        if not A:
            return 0
        ab_dic = dict()
        l = len(A)
        ans = 0
        for i in range(l):
            for j in range(l):
                a = A[i]
                b = B[j]
                ab_dic[a + b] = ab_dic.get(a + b, 0) + 1
        for i in range(l):
            for j in range(l):
                if -C[i] - D[j] in ab_dic:
                    ans += ab_dic[-C[i] - D[j]]
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.fourSumCount([-1,-1],[-1,1],[-1,1],[1,-1])
    print(b)
        
# @lc code=end

