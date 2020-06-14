#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

import collections
# @lc code=start
class Solution:
    def findOrder(self, numCourses, prerequisites):
        if not prerequisites:
            return [_ for _ in range(numCourses)]
        parent = collections.defaultdict(set)
        children = collections.defaultdict(int)
        for relation in prerequisites:
            parent[relation[0]].add(relation[1])
            children[relation[1]] += 1
        ans = collections.deque()
        for _ in range(numCourses):
            no_pre = False
            for no in range(numCourses):
                if children[no] == 0:
                    no_pre = True
                    ans.appendleft(no)
                    children[no] = -1
                    for pre in parent[no]:
                        children[pre] -= 1
            if no_pre == False and len(ans) < numCourses:
                return []
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.findOrder(2, [[0,1]])
    print(b)

# @lc code=end

