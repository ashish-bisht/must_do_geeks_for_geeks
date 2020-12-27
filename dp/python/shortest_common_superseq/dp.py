def shortest_common_superseq(string1, string2):
    col_length = len(string2)+1
    row_length = len(string1)+1
    matrix = [[0 for _ in range(col_length)] for _ in range(row_length)]

    for row in range(1, row_length):
        for col in range(1, col_length):
            if string1[row-1] == string2[col-1]:
                matrix[row][col] = 1 + matrix[row-1][col-1]

            else:
                matrix[row][col] = max(matrix[row-1][col], matrix[row][col-1])

    return len(string1) + len(string2) - matrix[-1][-1]


print(shortest_common_superseq("abcd", "xycd"))
print(shortest_common_superseq("efgh", "jghi"))
print(shortest_common_superseq("abcd", "lmno"))
print(shortest_common_superseq("abcd", "lmno"))
print(shortest_common_superseq("", ""))
