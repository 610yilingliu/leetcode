#
# @lc app=leetcode id=845 lang=python3
#
# [845] Longest Mountain in Array
#

# @lc code=start
class Solution:
    def longestMountain(self, A) -> int:
        tend = []
        for i in range(0, len(A) - 1):
            if A[i + 1] > A[i]:
                tend.append(1)
            elif A[i + 1] == A[i]:
                tend.append(0)
            else:
                tend.append(-1)
        peeks = []
        i = 0
        pre = 0
        tmp = 0
        has_up = 0
        while i < len(tend):
            if tend[i] == 0:
                if tmp > 0 and pre == -1:
                    peeks.append(tmp)
                pre = 0
                tmp = 0
                has_up = 0
            elif tend[i] == 1:
                if pre != -1:
                    tmp += 1
                    pre = 1
                    has_up = 1
                else:
                    if tmp > 0:
                        peeks.append(tmp)
                    pre = 1
                    has_up = 1
                    tmp = 1
            else:
                if has_up:
                    pre = -1
                    tmp += 1
            i += 1
        if tmp and pre == -1: peeks.append(tmp)
        return max(peeks) + 1 if peeks else 0

if __name__ == '__main__':
    a = Solution()
    b = a.longestMountain([0,1,2,3,4,5,4,3,2,1,0])
    print(b)
# @lc code=end

