def equal_subset(nums):
    if sum(nums) % 2 != 0:
        return False

    return helper(nums, sum(nums)//2, 0)


def helper(nums, total, index):
    if total == 0:
        return True

    if index >= len(nums):
        return False

    with_cur_num = helper(nums, total - nums[index], index+1)
    without_cur_num = helper(nums, total, index+1)
    return without_cur_num or with_cur_num


print("Can partition: " + str(equal_subset([1, 2, 3, 4])))
print("Can partition: " + str(equal_subset([1, 1, 3, 4, 7])))
print("Can partition: " + str(equal_subset([2, 3, 4, 6])))
