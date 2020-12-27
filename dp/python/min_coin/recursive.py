def min_coins(denoms, amount):
    return helper(denoms, amount, 0)


def helper(denoms, amount, index):
    if index >= len(denoms):
        return float("inf")
    if amount == 0:
        return 0

    with_cur_coin = float("inf")

    if amount >= denoms[index]:
        with_cur_coin = 1 + helper(denoms, amount-denoms[index], index)

    without_cur_coin = helper(denoms, amount, index+1)
    return min(with_cur_coin, without_cur_coin)


print(min_coins([1, 2, 5, 10, 20, 50, 100, 200, 500, 2000], 43))
print(min_coins([1, 2, 5], 17))
print(min_coins([1, 2, 5], 18))
print(min_coins([], 18))
