#
# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
import collections

class Solution:
    def getImportance(self, employees: List['Employee'], id: int):
        d = dict()
        i = dict()
        for employee in employees:
            d[employee.id] = employee.subordinates
            i[employee.id] = employee.importance
        ans = 0
        q = collections.deque([id])
        visited = set()
        while q:
            cur = q.popleft()
            visited.add(cur)
            ans += i[cur]
            for ele in d[cur]:
                if ele not in visited:
                    q.append(ele)
        return ans



    



# @lc code=end

