def min_jumps(nums):
    return helper(nums, 0, len(nums)-1)


def helper(nums, index, target):
    if target == index:
        return 0

    if nums[index] == 0:
        return float("inf")

    if index >= len(nums):
        return float("inf")

    min_jump = float("inf")
    for i in range(index+1, target+1):
        if (i < index + nums[index] + 1):
            jump = 1 + helper(nums, i, target)

            min_jump = min(min_jump, jump)

    return min_jump


print(min_jumps([2, 3, 1, 1, 4]))
print(min_jumps([2, 3, 0, 1, 4]))
