#
# @lc app=leetcode id=391 lang=python3
#
# [391] Perfect Rectangle
#

# @lc code=start
# class segtree:
#     def __init__(self, pos):
#         self.l = pos[0]
#         self.r = pos[2]
#         self.d = pos[1]
#         self.u = pos[3]
#         self.left = None
#         self.right = None
#         self.up = None
#         self.down = None

# class Solution:
#     def isRectangleCover(self, rectangles):
#         if not rectangles or not rectangles[0]:
#             return True
#         s = segtree(rectangles[0])
#         for rec in rectangles[1:]:
#             self.add(s, rec)
#         if s.left or s.right or s.up or s.down:
#             return False
#         return True

#     def merge(self, seg1, seg2):
#         if seg1.l <= seg2.l and seg1.r >= seg2.r and seg1.d <= seg2.d and seg1.u >= seg2.u:
#             if seg2 == seg1.left:
#                 seg1.left = None
#             if seg2 == seg1.right:
#                 seg1.right = None
#             if seg2 == seg1.up:
#                 seg1.up = None
#             if seg2 == seg1.down:
#                 seg1.down = None
#             return True
#         return False

#     def add(self, seg, pos):
#         cur_l, cur_r, cur_d, cur_u = pos[0], pos[2], pos[1], pos[3]
#         if cur_l >= seg.l and cur_r <= seg.r and cur_d >= seg.d and cur_u <= seg.u:
#             seg.l, seg.r, seg.d, seg.u = cur_l, cur_r, cur_d, cur_u
#             curl = seg.left
#             while curl:
#                 nowl = curl.left
#                 t = self.merge(seg, curl)
#                 curl = nowl
#                 if t == False:
#                     break
#             curr = seg.right
#             while curr:
#                 nowr = curr.right
#                 t = self.merge(seg, curr)
#                 curr = nowr
#                 if t == False:
#                     break
#             curu = seg.up
#             while curu:
#                 nowu = curu.up
#                 t = self.merge(seg, curu)
#                 curu = nowu
#                 if t == False:
#                     break
#             curd = seg.down
#             while curd:
#                 nowd = curd.down
#                 t = self.merge(seg, curd)
#                 curd = nowd
#                 if t == False:
#                     break
#         if cur_l < seg.l:
#             seg.left = segtree(pos)
#         elif cur_r > seg.r:
#             seg.right = segtree(pos)
#         if cur_u > seg.u:
#             seg.up = segtree(pos)
#         if cur_d < seg.d:
#             seg.down = segtree(pos)

# if __name__ == '__main__':
#     a = Solution()
#     b = a.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]])
#     print(b)

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]):
        """
        Idea is from Huahua jiang,
        The main idea is that except the four corners of perfect square, all other corners of sub rectangles all
        appeare even times
        """
        corners = set()
        area = 0
        for rect in rectangles:
            p1 = (rect[0], rect[1])
            p2 = (rect[0], rect[3])
            p3 = (rect[2], rect[1])
            p4 = (rect[2], rect[3])
            for p in [p1, p2, p3, p4]:
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)
            area += (p4[0] - p1[0]) * (p4[1] - p1[1])
        
        if len(corners) != 4:
            return False
        corners = sorted(list(corners))
        p1, p4 = corners[0], corners[-1]
        return area == (p4[0] - p1[0]) * (p4[1] - p1[1])
# @lc code=end

