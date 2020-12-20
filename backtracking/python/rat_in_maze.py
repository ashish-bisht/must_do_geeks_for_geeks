matrix = [[1, 0, 0, 0],
          [1, 1, 0, 1],
          [1, 1, 0, 0],
          [0, 1, 1, 1]]


def rat_in_maze(matrix):
    ans = []
    helper(matrix, [], ans, 0, 0)
    return ans


def helper(matrix, cur, res, row, col):

    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] != 1:
        return

    if row == len(matrix)-1 and col == len(matrix[row])-1:
        res.append(cur)
        return

    matrix[row][col] = 0

    helper(matrix, cur + ["U"], res, row-1, col)
    helper(matrix, cur + ["D"], res, row+1, col)
    helper(matrix, cur + ["L"], res, row, col-1)
    helper(matrix, cur + ["R"], res, row, col+1)
    matrix[row][col] = 1


print(rat_in_maze(matrix))
