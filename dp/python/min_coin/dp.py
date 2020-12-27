def min_coins(denoms, total):
    row_length = len(denoms)+1
    col_length = total + 1

    matrix = [[float("inf") for _ in range(col_length)]
              for _ in range(row_length)]

    for row in range(row_length):
        matrix[row][0] = 0

    for row in range(1, row_length):
        for col in range(1, col_length):
            if col >= denoms[row-1]:
                matrix[row][col] = min(
                    matrix[row-1][col], (1 + matrix[row][col - denoms[row-1]]))
            else:
                matrix[row][col] = matrix[row-1][col]

    return matrix[-1][-1]


print(min_coins([1, 2, 5, 10, 20, 50, 100, 200, 500, 2000], 43))
print(min_coins([1, 2, 5, 10, 20, 50, 100, 200, 500, 2000], 1000))
print(min_coins([1, 2, 5], 17))
print(min_coins([1, 2, 5], 18))
print(min_coins([], 18))
