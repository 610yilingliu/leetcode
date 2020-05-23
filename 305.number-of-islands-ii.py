#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#
# @lc code=start
# class uftree:
#     def __init__(self, m, n):
#         self.parent = {}
#         self.rank = {}
#         self.treenum = 0

#     def addnode(self, x, y):
#             curcode = self.encrypt(x, y)
#             self.parent[curcode] = curcode
#             self.rank[curcode] = 0
#             self.treenum += 1

#     def encrypt(self, m, n):
#         return m * n + m

    # def get_root(self, i):
    #     if self.parent[i] != self.parent[self.parent[i]]:
    #         self.parent[i] = self.get_root(self.parent[i])
    #     return self.parent[i]
    
#     def isconnected(self, node1, node2):
#         return self.getmyroot(node1) == self.getmyroot(node2)

#     def union(self, node1, node2):
#         root1 = self.getmyroot(node1)
#         root2 = self.getmyroot(node2)
#         if self.rank[root1] >= self.rank[root2]:
#             self.parent[root2] = root1
#             self.rank[root1] += 1
#         else:
#             self.parent[root1] = root2
#             self.rank[root2] += 1
#         s = set()
#         for k, v in self.parent.items():
#             s.add(v)
#         self.treenum = len(s)



# class Solution:
#     def numIslands2(self, m: int, n: int, positions):
#         dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#         ans = []
#         lands = [[0] * n for _ in range(m)]
#         uf = uftree(m, n)
#         for land in positions:
#             lands[land[1]][land[0]] = 1
#             uf.addnode(land[0], land[1])
#             for d in dirs:
#                 new_y = land[0] + d[0]
#                 new_x = land[1] + d[1]
#                 if 0 <= new_x < n and 0 <= new_y < n:
#                     if lands[new_y][new_x] == 1:
#                         node1 = uf.encrypt(new_x, new_y)
#                         node2 = uf.encrypt(land[1], land[0])
#                         uf.union(node1, node2)
#             ans.append(uf.treenum)
#         return ans

# if __name__ == '__main__':
#     a = Solution()
#     b = a.numIslands2(3, 3, [[0,0], [0,1], [1,2], [2,1]])
#     print(b)
class UnionFind:
    def __init__(self, m, n):
        self.father = {}
        for i in range(n):
            for j in range(m):
                id = self.converttoId(i,j,m);
                self.father[id] = id 

    def converttoId(self, x, y, m):
        return x*m + y
        
    def find(self, x):
            parent = self.father[x]
            while parent != self.father[parent]:
                parent = self.father[parent]
            return parent
        
    def compressed_find(self, x):
        parent = self.father[x]
        while parent != self.father[parent]:
            parent = self.father[parent]

        temp = -1;
        fa = self.father[x]
        while fa != self.father[fa]:
            temp = self.father[fa]
            self.father[fa] = parent
            fa = temp

        return parent

        
    def union(self, x, y):
            fa_x = self.find(x)
            fa_y = self.find(y)
            if fa_x != fa_y:
                self.father[fa_x] = fa_y
                
class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        dx = [0,-1, 0, 1]
        dy = [1, 0, -1, 0]
        island = [[0 for i in range(m)] for j in range(n)]
        ans = []
        uf = UnionFind(n, m)
        count = 0
        if operators != None:
            for i in range(len(operators)):
                count += 1
                x = operators[i][0]
                y = operators[i][1]
                if island[x][y] != 1:
                    island[x][y]  = 1
                    id = uf.converttoId(x, y, m)
                    # 计算上下左右四个点的位置
                    for j in range(4):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        if 0 <= nx and nx < n and 0 <= ny and ny < m and island[nx][ny] == 1:
                            nid = uf.converttoId(nx, ny, m)
                            fa = uf.find(id)
                            nfa = uf.find(nid)
                            if fa != nfa:
                                count -= 1
                                uf.union(id, nid)
                else:
                    count -= 1

                ans.append(count)
            return ans

if __name__ == '__main__':
    a = Solution()
    b = a.numIslands2(3, 3, [[0,0], [0,1], [1,2], [1,2]])
    print(b)
# @lc code=end

