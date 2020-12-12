def equilibrium_point(nums):
    left_sum = [nums[0]]
    right_sum = [nums[-1]]

    for i in range(1, len(nums)):
        cur_num = nums[i-1] + nums[i]
        left_sum.append(cur_num)

    for i in reversed(range(len(nums)-1)):
        cur_num = nums[i+1] + nums[i]
        right_sum.append(cur_num)

    for i in range(len(nums)):
        if left_sum[i] == right_sum[i]:
            return i

    return -1


print(equilibrium_point([1, 7, 3, 6, 5, 6]))
print(equilibrium_point([1, 2, 3]))


# def equilibrium_point1(nums):
#     left = 0
#     right = len(nums) - 1
#     left_sum = 0
#     right_sum = 0

#     while left <= right:

#     return -1


# print(equilibrium_point1([1, 7, 3, 6, 5, 6]))
# # print(equilibrium_point1([1, 2, 3]))
