#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
class uf:
    def __init__(self):
        self.parent = dict()
        self.level = dict()
    
    def addpoint(self, n):
        self.parent[n] = n
        self.level[n] = 0

    def getroot(self, n):
        if self.parent[n] != self.parent[self.parent[n]]:
            self.parent[n] = self.getroot(self.parent[n])
        return self.parent[n]

    def union(self, a, b):
        r1 = self.getroot(a)
        r2 = self.getroot(b)
        if self.level[r1] >= self.level[r2]:
            self.parent[r2] = r1
            self.level[r2] += 1
        else:
            self.parent[r1] = r2
            self.level[r1] += 1

    def isin(self, n):
        if n in self.parent:
            return True
        return False

class Solution:
    def countComponents(self, n: int, edges):
        if n == 0:
            return 0
        if not edges:
            return n
        directions = [-1, 1]
        u = uf()
        ans = 0
        walked = set()
        def conntopoint(toadd, existed):
            u.addpoint(toadd)
            u.union(toadd, existed)

        for item in edges:
            walked.add(item[0])
            walked.add(item[1])
            if u.isin(item[0]) and u.isin(item[1]):
                r0 = u.getroot(item[0])
                r1 = u.getroot(item[1])
                if r0 == r1:
                    continue
                else:
                    u.union(r0, r1)
                    ans -= 1
            elif u.isin(item[0]):
                conntopoint(item[1], item[0])
            elif u.isin(item[1]):
                conntopoint(item[0], item[1])
            else:
                u.addpoint(item[0])
                u.addpoint(item[1])
                u.union(item[0], item[1])
                ans += 1
        if n > len(walked):
            ans += n - len(walked)
        return ans
                
# @lc code=end

