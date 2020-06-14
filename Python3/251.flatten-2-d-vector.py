#
# @lc app=leetcode id=251 lang=python3
#
# [251] Flatten 2D Vector
#

# @lc code=start
import collections
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.ls = collections.deque()
        for item in v:
            for ele in item:
                self.ls.append(ele)
        



    def next(self) -> int:
        if self.ls:
            cur = self.ls.popleft()
            return cur
        

    def hasNext(self) -> bool:
        if self.ls:
            return True
        return False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

