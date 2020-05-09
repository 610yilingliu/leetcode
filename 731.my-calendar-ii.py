#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#
# @lc code=start
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendarTwo:
    def __init__(self):
        self.booked = list()
        self.overlaped = list()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for os, oe in self.overlaped:
            if max(os, start) < min(oe, end):
                return False
        for bs, be in self.booked:
            ss = max(bs, start)
            ee = min(be, end)
            if ss < ee:
                self.overlaped.append((ss, ee))
        self.booked.append((start, end))
        return True

            
            
if __name__ == '__main__':
    obj = MyCalendarTwo()
    ls = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
    for item in ls:
        res = obj.book(item[0], item[1])
        print(res)

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end

