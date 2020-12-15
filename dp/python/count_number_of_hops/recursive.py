
def number_of_hops(n):
    if n == 1 or n == 0:
        return 1

    if n == 2:
        return 2

    if n == 3:
        return 4

    return number_of_hops(n-1) + number_of_hops(n-2) + number_of_hops(n-3)


print(number_of_hops(3))
print(number_of_hops(4))
print(number_of_hops(5))
print(number_of_hops(0))
