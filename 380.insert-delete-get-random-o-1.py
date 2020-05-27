#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        self.vals = []
        self.length = 0

    def insert(self, val: int):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.d:
            self.d[val] = self.length
            self.length += 1
            self.vals.append(val)
            return True
        return False
        

    def remove(self, val: int):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.d:
            idx = self.d.pop(val)
            self.vals[idx] = self.vals[-1]
            self.vals.pop()
            if idx != len(self.vals):
                self.d[self.vals[idx]] = idx
            self.length -= 1
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        """
        idx = random.randint(0, self.length - 1)
        return self.vals[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

