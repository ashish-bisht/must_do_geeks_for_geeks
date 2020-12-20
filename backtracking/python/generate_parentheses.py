
def generate_parentheses(n):
    res = []
    helper(n, n, n, "", res)
    return res


def helper(n, left_remain, right_remain, cur, res):

    if left_remain > right_remain:
        return

    if left_remain < 0 or right_remain < 0:
        return

    if left_remain == 0 and right_remain == 0:
        res.append(cur)
        return

    helper(n, left_remain-1, right_remain, cur + "(", res)
    helper(n, left_remain, right_remain-1, cur + ")", res)


print(generate_parentheses(2))
