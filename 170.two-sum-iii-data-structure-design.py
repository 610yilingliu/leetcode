#
# @lc app=leetcode id=170 lang=python3
#
# [170] Two Sum III - Data structure design
#

# @lc code=start
import collections
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(int)

    def add(self, number: int):
        """
        Add the number to an internal data structure..
        """
        self.d[number] += 1
        

    def find(self, value: int):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for key, val in self.d.items():
            if value - key in self.d:
                if key * 2 == value and self.d[key] > 1:
                    return True
                elif key * 2 != value:
                    return True
        return False


        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# @lc code=end

