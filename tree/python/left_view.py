class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def left_view(root):

    que = [root]

    ans = []

    while que:
        cur_level_values = []
        next_level = []

        for cur_node in que:
            cur_level_values.append(cur_node.val)
            if cur_node.left:
                next_level.append(cur_node.left)

            if cur_node.right:
                next_level.append(cur_node.right)

        ans.append(cur_level_values)
        que = next_level

    left_v = []

    for level in ans:
        left_v.append(level[0])

    return left_v


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)


print(left_view(root))
