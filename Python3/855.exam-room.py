#
# @lc app=leetcode id=855 lang=python3
#
# [855] Exam Room
#

# @lc code=start
import bisect

class ExamRoom(object):
    
    def __init__(self, N):
        self.N, self.L = N, []

    def seat(self):
        N, L = self.N, self.L
        if not L: res = 0
        else:
            d, res = L[0], 0
            for a, b in zip(L, L[1:]):
                if (b - a) // 2 > d:
                    d, res = (b - a) // 2, (b + a) // 2
            if N - 1 - L[-1] > d: res = N - 1
        bisect.insort(L, res)
        return res

    def leave(self, p):
        if p in self.L:
            self.L.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
obj = ExamRoom(10)
param_1 = obj.seat()
param_2 = obj.seat()
param_3 = obj.seat()
obj.leave(5)
print(param_3)
# @lc code=end

