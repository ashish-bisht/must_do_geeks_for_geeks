def subset_sum(nums, total):
    return helper(nums, total, 0)


def helper(nums, total, index):
    if total == 0:
        return True

    if index >= len(nums):
        return False

    with_cur_num = helper(nums, total-nums[index], index+1)
    without_cur_num = helper(nums, total, index+1)

    return with_cur_num or without_cur_num


def main():
    print("Can partition: " + str(subset_sum([1, 2, 3, 7], 6)))
    print("Can partition: " + str(subset_sum([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(subset_sum([1, 3, 4, 8], 6)))
    print("Can partition: " + str(subset_sum([], 6)))
    print("Can partition: " + str(subset_sum([], 0)))
    print("Can partition: " + str(subset_sum([-1, 3, 4, 5], 2)))
    print("Can partition: " + str(subset_sum([1, 0, 4], 3)))


main()
