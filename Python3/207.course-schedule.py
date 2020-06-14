#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
import collections
# @lc code=start
class Solution:
    def canFinish(self, numCourses, prerequisites):
        child = collections.defaultdict(int)
        parent = collections.defaultdict(set)
        for item in prerequisites:
            parent[item[1]].add(item[0])
            child[item[0]] += 1
        for i in range(numCourses):
            has_zero = False
            for item in range(numCourses):
                if child[item] == 0:
                    has_zero = True
                    child[item] = -1
                    break
            if not has_zero:
                return False
            for thing in parent[item]:
                child[thing] -= 1
        return True



        
        
# @lc code=end

