def longest_increasing_subseq(nums):
    row_length = col_length = len(nums)-1

    matrix = [[0 for _ in range(col_length)] for _ in range(row_length)]

    for col in range(1, col_length):
        matrix[0][col] = 1

    for row in range(1, row_length):
        for col in range(1, col_length):
            if col > nums[row-1]:
                matrix[row][col] = 1 + matrix[row-1][col]
            else:
                matrix[row][col] = matrix[row-1][col]
    return matrix[-1][-1]


print(longest_increasing_subseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5,
                                 13, 3, 11, 7, 15]))
# print(longest_increasing_subseq([5, 8, 3, 7, 9, 1]))
# print(longest_increasing_subseq([8, 7, 6, 5, 4, 3, 2, 1]))
# print(longest_increasing_subseq([0]))
# print(longest_increasing_subseq([]))
# print(longest_increasing_subseq([10, 9, 2, 5, 3, 7, 101, 18]))
# print(longest_increasing_subseq([0, 1, 0, 3, 2, 3]))
# print(longest_increasing_subseq([7, 7, 7, 7, 7, 7, 7]))
