
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None

        self.right = None


def valid_bst(root):
    return helper(float("-inf"), root, float("inf"))


def helper(left_bound, root, right_bound):
    if not root:
        return True

    left = helper(left_bound, root.left, root.val)
    right = helper(root.val, root.right, right_bound)

    if not left_bound < root.val < right_bound:
        return False

    return left and right


root = Node(5)
root.left = Node(1)
root.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(6)

print(valid_bst(root))


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print(valid_bst(root))

root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(4)
print(valid_bst(root))


root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(4)

print(valid_bst(root))

root.left.right = Node(10)
print(valid_bst(root))
