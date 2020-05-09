#
# @lc app=leetcode id=732 lang=python3
#
# [732] My Calendar III
#

# @lc code=start
class Node:
    def __init__(self, start, end, count):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        self.multi = count

class MyCalendarThree:

    def __init__(self):
        self.root = None
        self.mx = 1

    def tree_helper(self, root, start, end, currentheight):
        if root is None:
            return Node(start, end, currentheight)

        if start >= root.end:
            root.right = self.tree_helper(root.right, start, end, currentheight)
        elif end <= root.start:
            root.left = self.tree_helper(root.left, start, end, currentheight)
        else:
            rgs = sorted([root.start, root.end, start, end])
            cur_l, cur_r = root.start, root.end
            root.start, root.end = rgs[1], rgs[2]
            root.left = self.tree_helper(root.left, rgs[0], rgs[1], currentheight if start < cur_l else root.multi)
            root.right = self.tree_helper(root.right, rgs[2], rgs[3], currentheight if end > cur_r else root.multi)
            root.multi += currentheight
            self.mx = max(self.mx, root.multi)
        return root



    def book(self, start: int, end: int):
        self.root = self.tree_helper(self.root, start, end, 1)
        return self.mx


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
# @lc code=end

