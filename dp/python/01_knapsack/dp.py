def dp_knapsack(weights, prices, max_allowed):

    col_length = max_allowed + 1
    row_length = len(weights)
    matrix = [[0 for _ in range(col_length)] for _ in range(row_length)]

    for row in range(1, row_length):
        for col in range(1, col_length):
            if col >= weights[row-1]:
                matrix[row][col] = max(prices[row-1] +
                                       matrix[row-1][col-weights[row-1]], matrix[row-1][col])
            else:
                matrix[row][col] = matrix[row-1][col]
    # print(matrix)
    return matrix[-1][-1]


print(dp_knapsack([1, 4, 5], [3, 1, 2], 4))
print(dp_knapsack([5, 6, 7], [3, 1, 2], 4))
print(dp_knapsack([1, 4, 5], [3, 1, 2], 5))
