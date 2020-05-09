#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
import collections
class Solution:
    def openLock(self, deadends, target):
        def neighbors(string):
            for idx in range(4):
                i = int(string[idx])
                for dist in (-1, 1):
                    nxt = (i + dist) % 10
                    yield string[:idx] + str(nxt) + string[idx + 1:]

        visited = {'0000'}
        storage = collections.deque([('0000', 0)])
        dead = set(deadends)
        while storage:
            curstr, cnt = storage.popleft()
            if curstr == target:
                return cnt
            if curstr in dead:
                continue
            for newele in neighbors(curstr):
                if newele not in visited:
                    visited.add(newele)
                    storage.append((newele, cnt + 1))
        return -1
            
if __name__ == '__main__':
    a = Solution()
    b = a.openLock(["0201","0101","0102","1212","2002"], '0202')
    print(b)
# @lc code=end

