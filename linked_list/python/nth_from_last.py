class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def nth_from_last(head, n):
    slow = fast = head

    while n > 0 and fast:
        fast = fast.next
        n -= 1

    if n > 0 and not fast:
        return "List ni hai bhai"
    if not fast:
        return head.val

    while fast:
        fast = fast.next
        slow = slow.next

    return slow.val


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(nth_from_last(head, 2))
print(nth_from_last(head, 5))
print(nth_from_last(head, 6))
