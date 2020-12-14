def longest_common_subseq(str1, str2):
    return helper(str1, str2, 0, 0)


def helper(str1, str2, index1, index2):
    if not str1:
        return 0

    if not str2:
        return 0

    if index1 >= len(str1) or index2 >= len(str2):
        return 0

    if str1[index1] == str2[index2]:
        return 1 + helper(str1, str2, index1+1, index2+1)

    return max(helper(str1, str2, index1+1, index2), helper(str1, str2, index1, index2+1))


print(longest_common_subseq("ABCDGH", "AEDFHR"))

print(longest_common_subseq("ABC", "AC"))

print(longest_common_subseq("ABC", "z"))
print(longest_common_subseq("ABC", ""))
