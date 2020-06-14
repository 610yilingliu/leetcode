#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#

# @lc code=start
class Segtree:
    def __init__(self, start, end, height):
        self.s = start
        self.e = end
        self.height = height
        self.left = None
        self.right = None

class Solution:
    mx = 1
    def tree_helper(self, root, start, end, height):
        if root is None:
            return Segtree(start, end, height)
        if end <= root.s:
            root.left = self.tree_helper(root.left, start, end, height)
        elif start >= root.e:
            root.right = self.tree_helper(root.right, start, end, height)

        else:
            rgs = sorted([root.s, root.e, start, end])
            cur_s, cur_e = root.s, root.e
            root.s, root.e = rgs[1], rgs[2]
            root.left = self.tree_helper(root.left, rgs[0], rgs[1], height if start < cur_s else root.height)
            root.right = self.tree_helper(root.right, rgs[2], rgs[3], height if end > cur_e else root.height)
            root.height += height
            self.mx = max(self.mx, root.height)
        return root

    def canAttendMeetings(self, intervals):
        root = None
        for item in intervals:
            root = self.tree_helper(root, item[0], item[1], 1)
            if self.mx > 1:
                return False
        return True
# @lc code=end

if __name__ == '__main__':
    a = Solution()
    b = a.canAttendMeetings([[7,10],[2,4]])
    print(b)