
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = float("-inf")

    def max_path_sum(self, root):
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root:
            return 0

        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))

        self.ans = max(self.ans, root.val + left + right)
        return root.val + max(left, right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    print("Maximum Path Sum: " + str(Solution().max_path_sum(root)))
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    root.right.right.left = Node(9)
    print("Maximum Path Sum: " + str(Solution().max_path_sum(root)))

    root = Node(-1)
    root.left = Node(-3)
    print("Maximum Path Sum: " + str(Solution().max_path_sum(root)))


main()
