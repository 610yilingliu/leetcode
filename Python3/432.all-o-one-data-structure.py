#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#
import collections
# @lc code=start
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.max_val = 0
        self.min_val = 0
        self.key_map = dict()
        self.val_map = collections.defaultdict(set)

    def inc(self, key: str):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.key_map:
            pre_val = self.key_map[key]
            # update max val
            if pre_val == self.max_val:
                self.max_val += 1
            self.val_map[pre_val].remove(key)
            # update min val
            if pre_val == self.min_val and not self.val_map[pre_val]:
                self.min_val += 1
            if not self.val_map[pre_val]:
                del self.val_map[pre_val]
            self.val_map[pre_val + 1].add(key)
            self.key_map[key] += 1
        else:
            self.min_val = 1
            self.key_map[key] = 1
            self.val_map[1].add(key)
            if self.max_val == 0:
                self.max_val = 1
        

    def dec(self, key: str):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.key_map:
            if self.key_map[key] == 1:
                del self.key_map[key]
                self.val_map[1].remove(key)
                if not self.val_map[1]:
                    del self.val_map[1]
                    self.min_val = min([val for val in self.val_map])
            else:
                preval = self.key_map[key]
                # update min val
                if preval == self.min_val:
                    self.min_val -= 1
                self.key_map[key] -= 1
                self.val_map[preval].remove(key)
                if not self.val_map[preval]:
                    del self.val_map[preval]
                if preval == self.max_val and not self.val_map[preval]:
                    self.max_val -= 1
                self.val_map[preval - 1].add(key)

        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        """
        if self.max_val != 0:
            return next(iter(self.val_map[self.max_val]))
        else:
            return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        """
        if self.min_val != 0:
            return next(iter(self.val_map[self.min_val]))
        else:
            return ""      


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# ls = ["a", "b", "b", "c", "c", "c"]
# for item in ls:
#     obj.inc(item)
# obj.dec("b")
# obj.dec("b")
# obj.dec("a")
# param_3 = obj.getMaxKey()
# print(param_3)
# param_4 = obj.getMinKey()
# print(param_4)
# @lc code=end

