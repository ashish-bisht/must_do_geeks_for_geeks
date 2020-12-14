def knapsack_01(profits, weights, capacity):

    row_len = len(weights)+1
    col_len = capacity+1

    matrix = [[0 for _ in range(col_len)] for _ in range(row_len)]

    for row in range(1, row_len):
        for col in range(1, col_len):
            if weights[row-1] <= col:
                matrix[row][col] = profits[row-1] + \
                    matrix[row-1][col-weights[row-1]]
            else:
                matrix[row][col] = matrix[row-1][col]
    return matrix[-1][-1]


def main():
    print(knapsack_01([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(knapsack_01([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
