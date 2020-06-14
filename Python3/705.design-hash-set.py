#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.perdimension = 1000
        self.matrix = [[] for _ in range(1000)]
        self.hasmx = False

    def row(self, key):
        return key // self.perdimension

    def col(self, key):
        return key % self.perdimension
        
    def add(self, key: int):
        if key < 1000000:
            r = self.row(key)
            c = self.col(key)
            if not self.matrix[r]:
                self.matrix[r] = [False] * self.perdimension
            self.matrix[r][c] = True
        else:
            self.hasmx = True

    def remove(self, key: int):
        if key < 1000000:
            r = self.row(key)
            c = self.col(key)
            if self.matrix[r] and self.matrix[r][c] == True:
                self.matrix[r][c] = False
        if key == 1000000:
            self.hasmx = False

    def contains(self, key: int):
        """
        Returns true if this set contains the specified element
        """
        if key == 1000000:
            if self.hasmx:
                return True
            return False
        r = self.row(key)
        c = self.col(key)
        if self.matrix[r] and self.matrix[r][c]:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end


