import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def tree_builder(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = collections.deque([root])
    leng = len(values)
    nums = 1
    while nums < leng:
             node = queue.popleft()
             if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1
    return root


def levelorder_list_of_list(root):
    lev_d = collections.defaultdict(list)
    mxlev = 0

    def travel(node, lev):
        if not node:
            return
        lev_d[lev].append(node.val)
        mxlev = max(lev, mxlev)

        travel(node.left, lev + 1)

        travel(node.right, lev + 1)

    travel(root, 0)

    res = [0] * mxlev
    for k, v in lev_d.items():
        res[k] = v
    return res



# given question: find the maimum size of an island

class play:
    def playing(self, matrix, x, y, stop):
        """
        @ type matrix: List[List]
        @ type x: Int, x-coordinate to input new chess piece
        @ type y: Int, y-coordinate to input new chess piece
        @ type stop: Int, how many chess piece required in one line
        """
        if not matrix or not matrix[0]:
            return False
        if x < 0 or x >= len(matrix) or y < 0 or y > len(matrix[0]):
            print("invalid place to put chess piece")
            return False

        self.matrix = matrix
        # search four direction seperately:
        # four directions:
        # 1. left and right
        # 2. up and down
        # 3. upper left and bottom right corner
        # 4. upper right and bottom left corner
        for direction in ("lr", "ud", "cor1", "cor2"):
            # everytime you have to reset the count to 0. 
            self.count = 0
            # the place for you to place new chess should be counted!!!!
            self.matrix[x][y] = 1
            self.searcher(x, y, direction, stop)
            if self.count == stop:
                return True
        return False

        
    def searcher(self, curx, cury, curdir, stop):
        # stop case: reach to not occupied cell
        if self.matrix[curx][cury] == 0:
            return
        # stop case: enough linked cells found
        if self.count == stop:
            return
        # if current cell is one, count + 1
        self.count += 1
        # set current cell to 0, avoid error from searching [1, 1, 1]: 1 go right to next 1, next 1 go to both left and right. so we have
        # to let walked cell become 0
        self.matrix[curx][cury] = 0
        # direction 1: left and right
        if curdir == "lr":
            for d in (1, -1):
                nxtx = curx + d
                if 0 <= nxtx < len(self.matrix):
                    self.searcher(nxtx, cury, curdir, stop)
        # direction 2: up and down
        if curdir == 'ud':
            for d in (1, -1):
                nxty = cury + d
                if 0 <= nxty < len(self.matrix[0]):
                    self.searcher(curx, nxty, curdir, stop)
        # direction 3 and 4
        if curdir == 'cor1':
            to_cor1 = [(-1, 1), (1, -1)]
            for d in to_cor1:
                nxtx = curx + d[0]
                nxty = cury + d[1]
                if 0 <= nxtx < len(self.matrix) and 0 <= nxty < len(self.matrix[0]):
                    self.searcher(nxtx, nxty, curdir, stop)
            to_cor2 = [(1, 1), (-1, -1)]
        else:
            for d in to_cor2:
                nxtx = curx + d[0]
                nxty = cury + d[1]
                if 0 <= nxtx < len(self.matrix) and 0 <= nxty < len(self.matrix[0]):
                    self.searcher(nxtx, nxty, curdir, stop)       

                
a = play()
b = a.playing([[0, 1, 1],
[1, 0, 0],
[1, 0, 0]], 1, 1, 3)
print(b)




