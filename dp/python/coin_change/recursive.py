def coin_change(coins, total):
    return helper(coins, total, 0)


def helper(coins, total, index):
    if total == 0:
        return 1

    if len(coins) == 0 or index >= len(coins):
        return 0

    with_cur_coin = 0

    if coins[index] <= total:
        with_cur_coin = helper(coins, total-coins[index], index)

    without_cur_coin = helper(coins, total, index+1)

    return with_cur_coin + without_cur_coin


print(coin_change([2, 5, 3, 6], 10))
