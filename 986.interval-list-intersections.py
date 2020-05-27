#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(self, A, B):
        if not A or not B:
            return []
        cur1 = 0
        cur2 = 0
        end1 = len(A)
        end2 = len(B)
        ans = []
        while cur1 < end1 and cur2 < end2:
            if A[cur1][1] < B[cur2][0]:
                cur1 += 1
            elif B[cur2][1] < A[cur1][0]:
                cur2 += 1
            else:
                intersect = self.intersection(A[cur1], B[cur2])
                ans.append(intersect)
                if A[cur1][1] < B[cur2][1]:
                    cur1 += 1
                elif A[cur1][1] > B[cur2][1]:
                    cur2 += 1
                else:
                    cur1 += 1
                    cur2 += 1
        return ans
        
    def intersection(self, rg1, rg2):
        mi1, mx1, mi2, mx2 = rg1[0], rg1[1], rg2[0], rg2[1]
        if mx1 == mi2:
            return [mx1, mx1]
        if mi1 == mx2:
            return [mx2, mx2]
        start = max(mi1, mi2)
        end = min(mx1, mx2)
        return [start, end]

# if __name__ == '__main__':
#     a = Solution()
#     b = a.intervalIntersection(A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]])
#     print(b)
# @lc code=end

