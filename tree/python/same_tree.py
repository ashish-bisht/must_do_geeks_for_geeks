#      1                1
#     / \              / \
#    2   3            2   3


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_same_tree(root1, root2):
    if not root1 and not root2:
        return True

    if root1 and not root2:
        return False

    if root2 and not root1:
        return False

    if root1.val != root2.val:
        return False

    left = is_same_tree(root1.left, root2.left)
    right = is_same_tree(root1.right, root2.right)

    return left and right


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)


root2 = Node(1)
root2.left = Node(2)
root2.right = Node(4)


print(is_same_tree(root1, root2))
root2.right = Node(3)

print(is_same_tree(root1, root2))
