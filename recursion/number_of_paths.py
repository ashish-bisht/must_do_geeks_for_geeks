def number_of_paths(row, col):

    if row == 1 and col == 1:
        return 1

    if row < 0 or col < 0:
        return 0

    return number_of_paths(row-1, col) + number_of_paths(row, col-1)


print("*********************Normal Recursive************************")
print(number_of_paths(3, 7))
print(number_of_paths(3, 2))
print(number_of_paths(3, 3))


def number_of_paths_cache(row, col):
    cache = {}

    if (row, col) in cache:
        return cache[(row, col)]

    if row == 1 and col == 1:
        return 1

    if row < 0 or col < 0:
        return 0

    cache[(row, col)] = number_of_paths(
        row-1, col) + number_of_paths(row, col-1)

    return cache[(row, col)]


print("*********************Recursive with Cache************************")

print(number_of_paths_cache(3, 7))
print(number_of_paths_cache(3, 2))
print(number_of_paths_cache(3, 3))


def number_of_paths_dp(num_row, num_col):
    matrix = [[1 for _ in range(num_col)] for _ in range(num_row)]

    for row in range(1, num_row):
        for col in range(1, num_col):
            matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]

    return matrix[-1][-1]


print("*********************DP************************")
print(number_of_paths_dp(3, 7))
print(number_of_paths_dp(3, 2))
print(number_of_paths_dp(3, 3))
