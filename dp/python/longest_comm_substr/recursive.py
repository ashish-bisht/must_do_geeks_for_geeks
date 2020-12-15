def longest_common_substring(str1, str2):
    return helper(str1, str2, 0, 0, 0)


def helper(str1, str2, index1, index2, count):

    if index1 >= len(str1) or index2 >= len(str2):
        return count

    if str1[index1] == str2[index2]:
        count = helper(str1, str2, index1+1, index2+1, count+1)

    return (max(count, (max(helper(str1, str2, index1, index2+1, 0), helper(str1, str2, index1+1, index2, 0)))))


print(longest_common_substring("abdca", "cbda"))
print(longest_common_substring("passport", "ppsspt"))
print(longest_common_substring("aca", "ca"))
