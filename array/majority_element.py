from collections import Counter


def majority_element(nums):

    nums_counter = Counter(nums)

    for key, val in nums_counter.items():
        if val >= len(nums)/2:
            return key

    return "Not Possible"


print(majority_element([1, 2, 3]))
print(majority_element([3, 1, 3, 3, 2]))
