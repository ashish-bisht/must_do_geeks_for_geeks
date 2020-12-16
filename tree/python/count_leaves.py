#        4
#      /   \
#     8     10
#    /     /   \
#   7     5     1
#  /
# 3

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1

    left = count_leaves(root.left)
    right = count_leaves(root.right)

    return left + right


root = Node(4)
root.left = Node(8)
root.right = Node(10)
root.left.left = Node(7)
root.right.left = Node(5)
root.left.left.left = Node(3)
root.right.right = Node(1)

print(count_leaves(root))  # 3
