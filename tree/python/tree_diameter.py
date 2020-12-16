class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:
    ans = 0

    def get_diameter(self, root):
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        self.ans = max(self.ans, 1+left+right)

        return 1 + max(left, right)


def main():
    treeDiameter = TreeDiameter()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    print("Tree Diameter: " + str(TreeDiameter().get_diameter(root)))
    root.left.left = None
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    root.right.right.left = Node(9)
    root.right.left.right.left = Node(10)
    root.right.right.left.left = Node(11)
    print("Tree Diameter: " + str(TreeDiameter().get_diameter(root)))


main()
