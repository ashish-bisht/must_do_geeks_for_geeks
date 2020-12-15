def max_sum_inc_subseq(nums):
    return helper(nums, 0, float("-inf"))


def helper(nums, index, last_num):
    if index >= len(nums):
        return 0

    with_cur_num = 0

    if nums[index] > last_num:
        with_cur_num = nums[index] + helper(nums, index+1, nums[index])

    without_cur_num = helper(nums, index+1, last_num)

    return max(with_cur_num, without_cur_num)


print(max_sum_inc_subseq([4, 1, 2, 6, 10, 1, 12]))
print(max_sum_inc_subseq([-4, 10, 3, 7, 15]))
