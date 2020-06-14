#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
import collections
class Solution:
    def findJudge(self, N, trust):
        map1 = collections.defaultdict(list)
        map2 = collections.defaultdict(list)
        for i in range(len(trust)):
            map1[trust[i][0]].append(trust[i][1])
            map2[trust[i][1]].append(trust[i][0])
        for num in range(1, N + 1):
            if num not in map1:
                if len(map2[num]) == N - 1:
                    return num
        return -1
# @lc code=end

