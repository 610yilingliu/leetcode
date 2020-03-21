def mat(matrix):
    l = len(matrix)
    # 最大面积初始化为0
    area = 0
    x = 0
    y = 0
    while x < l and y < l:
        temp_area, step = helper2(matrix, x, y)
        x = x + step
        if temp_area > area:
            area = temp_area
    return area

def helper(matrix):
    l = len(matrix)
    area = 0
    for i in range(l):
        for j in range(l):
            if matrix[i][j] == 0:
                area = min(i,j) ** 2
                return area, min(i,j)
    return l * l, l

def helper2(matrix, ori_x, ori_y):
    l = len(matrix)
    max_area = 0
    for i in range(ori_x, l):
        for j in range(ori_y, l):
            if matrix[i][j] == 1:
                # 如果 (i,j)为1，记为初始点，由此点开始搜索
                start_x = i
                start_y = j
                # 如果不为最后一列
                if start_x < l - 1:
                    # 向右搜索最近的一个为0的点
                    end_x = -1
                    for a in range(start_x, l):
                        if matrix[a][start_y] == 0:
                            #记为终点
                            end_x = a - 1
                            # 如果这个终点就在初始点右边，则将面积记为1（初始点为孤立点或一条竖线的形状）
                            if end_x == start_x:
                                temp_area = 1
                                if temp_area > max_area:
                                    max_area = temp_area
                    # 如果找不到，就用矩阵最右边的坐标
                    if end_x == -1:
                        end_x = l - 1
                if start_y < l - 1:
                    end_y = -1
                    for b in range(start_y, l):
                        if matrix[start_x][b] == 0:
                            end_y = b - 1
                            if end_y == start_y:
                                temp_area = 1
                                if temp_area > area:
                                    area = temp_area
                    if end_y == -1:
                        end_y = l - 1
                dis = min(end_x - start_x, end_y - start_y)
                new_matrix = [item[start_y: end_y] for item in matrix[start_x: start_x + dis]]
                temp_area, step = helper(new_matrix)
                if temp_area > max_area:
                    max_area = temp_area
    return max_area, step