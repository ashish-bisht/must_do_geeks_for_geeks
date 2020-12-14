def knapsack_01(profits, weights, capacity):
    return helper(profits, weights, capacity, 0)


def helper(profits, weights, capacity, index):

    if capacity <= 0 or index >= len(weights):
        return 0
    profit_with_curr_index = 0

    if weights[index] <= capacity:

        profit_with_curr_index = profits[index] + helper(
            profits, weights, capacity - weights[index], index+1)

    profit_without_curr_index = helper(profits, weights, capacity, index+1)

    return max(profit_with_curr_index, profit_without_curr_index)


def main():
    print(knapsack_01([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(knapsack_01([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
