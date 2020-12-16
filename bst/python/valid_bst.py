class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def valid_bst(root):
    return helper(float("-inf"), root, float("inf"))


def helper(left, root, right):
    if not root:
        return True

    if not left < root.val < right:
        return False

    left = helper(left, root.left, root.val)
    right = helper(root.val, root.right, right)
    return left and right


root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(4)

print(valid_bst(root))

root.left.right = Node(10)
print(valid_bst(root))
