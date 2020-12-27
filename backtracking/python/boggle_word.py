words = {"GEEKS", "FOR", "QUIZ", "GO"}
matrix = [['G', 'I', 'Z'],
          ['U', 'E', 'K'],
          ['Q', 'S', 'E']]


def word_matrix(words, matrix):
    res = set()
    for word in words:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if word in res:
                    break
                if matrix[row][col] == word[0]:
                    dfs(matrix, row, col, word, res, word)
            if word in res:
                break
    return res


def dfs(matrix, row, col, word, res, orginal):

    if not word:
        res.add(orginal)
        return

    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] != word[0]:
        return

    temp = matrix[row][col]
    matrix[row][col] = "#"

    dfs(matrix, row-1, col, word[1:], res, orginal)
    dfs(matrix, row+1, col, word[1:], res, orginal)
    dfs(matrix, row, col-1, word[1:], res, orginal)
    dfs(matrix, row, col+1, word[1:], res, orginal)
    dfs(matrix, row-1, col-1, word[1:], res, orginal)
    dfs(matrix, row+1, col+1, word[1:], res, orginal)
    dfs(matrix, row+1, col-1, word[1:], res, orginal)
    dfs(matrix, row-1, col+1, word[1:], res, orginal)
    matrix[row][col] = temp


print(word_matrix(words, matrix))
