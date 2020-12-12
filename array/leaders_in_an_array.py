def leaders_in_an_array(nums):
    leaders = [nums[-1]]

    max_so_far = nums[-1]

    for i in reversed(range(len(nums))):
        if max_so_far < nums[i]:
            max_so_far = nums[i]
            leaders.append(nums[i])

    return leaders


print(leaders_in_an_array([16, 17, 4, 3, 5, 2]))
print(leaders_in_an_array([1, 2, 3, 4, 0]))
