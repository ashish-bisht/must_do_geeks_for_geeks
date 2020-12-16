#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def invert_binary_tree(root):
    if not root:
        return

    root.left, root.right = root.right, root.left
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)


root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)

print(invert_binary_tree(root))
