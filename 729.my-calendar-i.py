#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#
import collections
# @lc code=start
class MyCalendar:

    def __init__(self):
        self.calender = collections.defaultdict(int)

    def book(self, start, end):
        for curstart in self.calender:
            curend = self.calender[curstart]
            if (curstart <= start and curend > start) or (curstart >= start and curstart < end):
                return False
        self.calender[start] = end
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

