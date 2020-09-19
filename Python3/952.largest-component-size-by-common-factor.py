#
# @lc app=leetcode id=952 lang=python3
#
# [952] Largest Component Size by Common Factor
#

# @lc code=start
import math
import collections

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        mx = max(A)
        m = list(range(mx + 1))
        for num in A:
            for f in range(2, int(math.sqrt(num)) + 1):
                if num % f == 0:
                    self.union(m, num, f)
                    self.union(m, num, num // f)
        cnt = collections.defaultdict(int)
        for a in A:
            cnt[self.find(m, a)] += 1
        return max(cnt.values())  

    def find(self, m, num):
        while m[num] != num:
            m[num] = m[m[num]]
            num = m[num]
        return num

    def union(self, m, num1, num2):
        if m[num1] == m[num2]:
            return
        root1 = self.find(m, num1)
        root2 = self.find(m, num2)
        m[root1] = root2



# @lc code=end

