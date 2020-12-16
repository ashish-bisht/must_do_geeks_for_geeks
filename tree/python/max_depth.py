#     3
#    / \
#   9  20
#     /  \
#    15   7


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_depth(root):
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return 1 + max(left, right)


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(max_depth(root))
