class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_palindrome(head):
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev = None

    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    while prev:
        if head.val != prev.val:
            return False

        prev = prev.next
        head = head.next
    return True


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(3)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(1)

print(is_palindrome(head))
