#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start
import collections
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]):
        graph = collections.defaultdict(list)
        for dislike in dislikes:
            # 1 -> n map to 0 -> n - 1, for putting them it into a list
            graph[dislike[0] - 1].append(dislike[1] - 1)
            graph[dislike[1] - 1].append(dislike[0] - 1)
        camp = [0] * N
        for i in range(N):
            # if already in camp
            if camp[i] != 0:
                continue
            bfs = collections.deque()
            bfs.append(i)
            camp[i] = 1
            while bfs:
                cur = bfs.popleft()
                for node in graph[cur]:
                    if camp[node] != 0:
                        # if in the same camp
                        if camp[node] == camp[cur]:
                            return False
                    else:
                        camp[node] = -camp[cur]
                        bfs.append(node)
        return True


# @lc code=end

