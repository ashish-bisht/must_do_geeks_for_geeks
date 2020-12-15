def largest_increasing_subseq(nums):
    return helper(nums, 0, float("-inf"))


def helper(nums, index, last_num):
    if index >= len(nums):
        return 0

    with_cur_num = 0

    if nums[index] > last_num:
        with_cur_num = 1 + helper(nums, index+1, nums[index])

    without_cur_num = helper(nums, index+1, last_num)

    return max(with_cur_num, without_cur_num)


print(largest_increasing_subseq([4, 2, 3, 6, 10, 1, 12]))
print(largest_increasing_subseq([-4, 10, 3, 7, 15]))
print(largest_increasing_subseq([-4]))
print(largest_increasing_subseq([]))
