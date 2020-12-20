matrix = [["o", "a", "a", "n"],
          ["e", "t", "a", "e"],
          ["i", "h", "k", "r"],
          ["i", "f", "l", "v"]]

words = ["oath", "pea", "eat", "rain"]


def word_search(matrix, words):
    res = []
    for word in words:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == word[0]:
                    dfs(matrix, row, col, word, "", res)
                    if word in res:
                        break
            if word in res:
                break

    return res


def dfs(matrix, row, col, word, cur, res):
    if not word:
        if cur not in res:
            res.append(cur)
        return

    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or word[0] != matrix[row][col]:
        return

    temp = matrix[row][col]
    matrix[row][col] = "#"

    # traverse in all directions::

    dfs(matrix, row-1, col, word[1:], cur + temp, res)
    dfs(matrix, row+1, col, word[1:], cur + temp, res)
    dfs(matrix, row, col-1, word[1:], cur + temp, res)
    dfs(matrix, row, col+1, word[1:], cur + temp, res)

    matrix[row][col] = temp


print(word_search(matrix, words))
