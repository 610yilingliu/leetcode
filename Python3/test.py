import collections
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        def valid(curr, curc):
            if curr < 0 or curr > N - 1 or curc < 0 or curc > N - 1:
                return False
            return True
        
        if valid(r, c) == False:
            return 0
        if K == 0:
            return 1
        bfs = collections.deque([(r, c, 0, True)])
        dirs = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
        out_cnt = 0
        in_cnt = 0
        while bfs and bfs[0][2] < K:
            curr, curc, curt, curvalid = bfs.popleft()
            for dir in dirs:
                if curvalid == False:
                    if curt + 1 == K:
                        out_cnt += 1
                    bfs.append((curr + dir[0], curc + dir[1], curt + 1, False))
                else:
                    nxtr = curr + dir[0]
                    nxtc = curc + dir[1]
                    is_valid = valid(nxtr, nxtc)
                    if is_valid and curt + 1 == K:
                        in_cnt += 1
                    else:
                        if curt + 1 == K:
                            out_cnt += 1
                    bfs.append((nxtr, nxtc, curt + 1, is_valid))
                    
        return in_cnt/(in_cnt + out_cnt)

a = Solution()
b = a.knightProbability(3, 2, 0, 0)
print(b)