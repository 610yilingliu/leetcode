#
# @lc app=leetcode id=281 lang=python3
#
# [281] Zigzag Iterator
#

# @lc code=start
class ZigzagIterator:
    def __init__(self, v1, v2):
        self.ls = []
        self.pos = 0
        if not v1 and not v2:
            return
        elif not v1:
            self.ls = v2
        elif not v2:
            self.ls = v1
        else:
            l1 = len(v1)
            l2 = len(v2)
            if l1 == l2:
                for i in range(l1):
                    self.ls.append(v1[i])
                    self.ls.append(v2[i])
            elif l1 > l2:
                for i in range(l2):
                    self.ls.append(v1[i])
                    self.ls.append(v2[i])
                self.ls += v1[i + 1:]
            else:
                for i in range(l1):
                    self.ls.append(v1[i])
                    self.ls.append(v2[i])
                self.ls += v2[i + 1:]


    def next(self):
        if self.ls:
            tmp = self.ls[self.pos]
            self.pos += 1
            return tmp

    def hasNext(self):
        if self.pos < len(self.ls):
            return True
        return False

    # def ret(self):
    #     return self.ls

# Your ZigzagIterator object will be instantiated and called as such:
# i = ZigzagIterator([1,2], [3])
# a = i.ret()
# print(a)
# while i.hasNext(): v.append(i.next())
# @lc code=end

