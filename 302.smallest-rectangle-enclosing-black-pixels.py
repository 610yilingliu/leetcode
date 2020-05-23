#
# @lc app=leetcode id=302 lang=python3
#
# [302] Smallest Rectangle Enclosing Black Pixels
#

# @lc code=start
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """

        min_x, max_x, min_y, max_y = self.getMinMaxCoords(image, x, y)
        
        x_diff = 1 + (max_x - min_x)
        y_diff = 1 + (max_y - min_y)
        
        return x_diff * y_diff
        
    def getMinMaxCoords(self, image, first_x, first_y):
        # Return values
        min_x, max_x, min_y, max_y = first_x, first_x, first_y, first_y

        # The highest valid x and y values in the image
        last_x_cell = len(image) - 1
        last_y_cell = len(image[0]) - 1

        # Seen is a set of tuples with every pixel we've visited
        seen = set()

        # Path is a list of tuples we need to check
        path = []
        path.append((first_x, first_y))

        
        while path:

            this_cell = path.pop()
            if this_cell in seen:
                continue

            seen.add(this_cell)

            x, y = this_cell[0], this_cell[1]

            # The ifs in the following statements look a bit ugly.
            # However, their nested nature speeds things up by allowing us to
            #  stop looking at a cell as soon as we know it is not promising.
            
            # Checks we make to see if we can stop looking:
            # - Is the new x or y value valid?
            # - Is the cell pointed to by the new (x, y) a "1"?
            # - Have we seen the cell before?
            # After those have been passed:
            # - If we're looking at a new min/max, update appropriately
            # - Add the new cell to the search

            # Look at left-adjacent cell
            if x > 0:
                if image[x-1][y] == "1":
                    if (x-1, y) not in seen:
                        if x - 1 < min_x:
                            min_x = x - 1
                        path.append((x-1, y))
            # Right
            if x < last_x_cell:
                if image[x+1][y] == "1":
                    if (x+1, y) not in seen:
                        if x + 1 > max_x:
                            max_x = x + 1
                        path.append((x+1, y))
            # Up
            if y > 0:
                if image[x][y-1] == "1":
                    if (x, y-1) not in seen:
                        if y - 1 < min_y:
                            min_y = y - 1
                        path.append((x, y-1))
            # Down
            if y < last_y_cell:
                if image[x][y+1] == "1":
                    if (x, y+1) not in seen:
                        if y + 1 > max_y:
                            max_y = y + 1
                        path.append((x, y+1))

        return min_x, max_x, min_y, max_y



# @lc code=end

