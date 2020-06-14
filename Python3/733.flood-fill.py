#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        if not image or not image[0]:
            return image
        rep = image[sr][sc]
        if rep == newColor:
            return image
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        h = len(image)
        l = len(image[0])

        def replacement(x, y):
            image[y][x] = newColor
            for d in dirs:
                new_x = x + d[0]
                new_y = y + d[1]
                if 0 <= new_x < l and 0 <= new_y < h:
                    if image[new_y][new_x] == rep:
                        replacement(new_x, new_y)
        replacement(sc, sr)
        return image

# if __name__ == '__main__':
#     a = Solution()
#     b = a.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
#     print(b)

# @lc code=end

