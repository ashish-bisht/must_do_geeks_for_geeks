# Time O(n) , space (1)

def missing_number(arr):
    # calculate sum
    total_numbers = len(arr)+1
    expected_sum = total_numbers*(total_numbers+1)//2

    actual_sum = 0

    for num in arr:
        actual_sum += num

    return expected_sum - actual_sum


print(missing_number([1, 2, 3, 5]))
print(missing_number([1, 2, 3, 4, 5, 6, 7, 8, 10]))


def missing_number_xor(arr):

    missing_number = len(arr)

    for i in range(len(arr)):
        missing_number ^= arr[i]
        missing_number ^= i

    return missing_number


print(missing_number_xor([0, 1, 2, 3, 5]))
print(missing_number_xor([0, 1, 2, 3, 4, 5, 6, 7, 8, 10]))
