def edit_distance(str1, str2):
    return helper(str1, str2, 0, 0)


def helper(str1, str2, index1, index2):

    if index1 == len(str1):
        return len(str2) - index2

    if index2 == len(str2):
        return len(str1) - index1

    if str1[index1] == str2[index2]:
        return helper(str1, str2, index1+1, index2+1)

    insertion = 1 + helper(str1, str2, index1, index2+1)
    deletion = 1 + helper(str1, str2, index1+1, index2)
    replace = 1 + helper(str1, str2, index1+1, index2+1)

    return min(insertion, deletion, replace)


print(edit_distance("geek", "gesek"))
print(edit_distance("bat", "but"))
print(edit_distance("abdca", "cbda"))
print(edit_distance("passpot", "ppsspqrt"))
