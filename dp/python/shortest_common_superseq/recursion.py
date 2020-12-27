def shortest_common_superseq(string1, string2):

    longest_common = common_seq(string1, string2, 0, 0)
    return len(string1) + len(string2) - longest_common


def common_seq(string1, string2, index1, index2):
    if not string1 or not string2:
        return 0

    if index1 >= len(string1) or index2 >= len(string2):
        return 0

    if string1[index1] == string2[index2]:
        return 1 + common_seq(string1, string2, index1+1, index2+1)

    return max(common_seq(string1, string2, index1+1, index2), common_seq(string1, string2, index1, index2+1))


print(shortest_common_superseq("abcd", "xycd"))
print(shortest_common_superseq("efgh", "jghi"))
print(shortest_common_superseq("abcd", "lmno"))
print(shortest_common_superseq("abcd", "lmno"))
print(shortest_common_superseq("", ""))
