import collections

class Solution:
    def min_distance(self, graph):
        """
        @Question to ask: int or string in graph?
        @We assume type graph: List[List[int]]
        """
        # case: graph is None or graph == []
        if not graph:
            return
        # case: graph == [[]]
        if not graph[0]:
            return
        # maximun of x is m - 1
        m = len(graph[0])
        # maximun of y is n - 1
        n = len(graph)
        start = None
        end = None
        doors = collections.defaultdict(list)

        for i in range(n):
            for j in range(m):
                if graph[i][j] == -2:
                    start = (i, j)
                elif graph[i][j] == -3:
                    end = (i, j)
                else:
                    doors[graph[i][j]].append((i, j))             
        # if not entry or exit exists
        if not start or not end:
            return

        dq = collections.deque()
        dq.append((0, start[0], start[1]))
        graph[start[0]][start[1]] = None
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while dq:
            cur_step, cur_y, cur_x = dq.popleft()
            graph[cur_y][cur_x] = None
            if cur_y == end[0] and cur_x == end[1]:
                return cur_step
            # case 1: 前后左右
            for d in directions:
                nxt_y = cur_y + d[0]
                nxt_x = cur_x + d[1]
                if nxt_x > 0 and nxt_x < m and nxt_y >= 0 and nxt_y < n and graph[nxt_y][nxt_x] != None:
                    dq.append((cur_step + 1, nxt_y, nxt_x))
            if graph[cur_y][cur_x] != 0:
                for item in doors[graph[cur_y][cur_x]]:
                    if item != (cur_y, cur_x):
                        nxt_y = item[0]
                        nxt_x = item[1]
                        if graph[nxt_y][nxt_x] != None:
                            dq.append((cur_step + 1, nxt_y, nxt_x))

if __name__ == '__main__':
    a = Solution()
    b = a.min_distance([[1,0,-1,1],[-2,0,-1,-3],[2,2,0,0]])
    print(b)