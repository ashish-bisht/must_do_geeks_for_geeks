def longest_increasing_subseq(nums):
    return helper(nums, 0, float("-inf"))


def helper(nums, index, last_num):
    if index >= len(nums):
        return 0

    with_cur = 0

    if last_num < nums[index]:
        with_cur = 1 + helper(nums, index+1, nums[index])

    without_cur = helper(nums, index+1, last_num)

    return max(with_cur, without_cur)


print(longest_increasing_subseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5,
                                 13, 3, 11, 7, 15]))
print(longest_increasing_subseq([5, 8, 3, 7, 9, 1]))
print(longest_increasing_subseq([8, 7, 6, 5, 4, 3, 2, 1]))
print(longest_increasing_subseq([0]))
print(longest_increasing_subseq([]))
print(longest_increasing_subseq([10, 9, 2, 5, 3, 7, 101, 18]))
print(longest_increasing_subseq([0, 1, 0, 3, 2, 3]))
print(longest_increasing_subseq([7, 7, 7, 7, 7, 7, 7]))
