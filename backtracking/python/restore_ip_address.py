def restore_ip_address(string):
    res = []

    helper(string, 0, "", res)
    return res


def helper(string, index, cur, res):
    if index > 4:
        return

    if index == 4 and not string:
        res.append(cur[:-1])
        return

    for i in range(1, len(string)+1):
        if string[:i] == "0" or string[0] != "0" and 0 < int(string[:i]) < 256:
            helper(string[i:], index+1, cur + string[:i]+".", res)


print(restore_ip_address("25525511135"))
print(restore_ip_address("0000"))
print(restore_ip_address("101023"))
