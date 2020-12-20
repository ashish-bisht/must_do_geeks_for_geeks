def permutations(nums):
    all_permutations = []
    helper(nums, [], all_permutations)
    return all_permutations


def helper(nums, cur, all_permutations):

    # backtack
    if not nums:
        all_permutations.append(cur)
        return

    # going through all

    for i in range(len(nums)):
        helper(nums[:i] + nums[i+1:], cur + [nums[i]], all_permutations)


print("Permutations are :", permutations([1, 2, 3]))
print("Permutations are :", permutations([]))
print("Permutations are :", permutations([1]))
print("Permutations are :", permutations([0, 1]))
