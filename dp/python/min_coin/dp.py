def min_coin(coins, amount):
    return helper(coins, amount, 0)


def helper(coins, amount, index):
    if not coins or index >= len(coins):
        return float("inf")

    if amount == 0:
        return 0

    with_cur_coin = float("inf")

    if coins[index] <= amount:
        with_cur_coin = 1 + helper(coins, amount - coins[index], index)

    without_cur_coin = helper(coins, amount, index+1)

    return min(with_cur_coin, without_cur_coin)


print(min_coin([1, 2, 3], 5))
print(min_coin([1, 2, 3], 11))
print(min_coin([1, 2, 3], 7))
print(min_coin([3, 5], 7))
