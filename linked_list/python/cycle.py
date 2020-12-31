class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head
print(is_cycle(head))


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print(is_cycle(head))
