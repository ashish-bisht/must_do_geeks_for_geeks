arr = [1, 2, 3, 4, 5, 6]


def square(num):
    return num*num


result = list(map(square, arr))
print(result)
