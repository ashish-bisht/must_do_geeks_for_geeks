class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linked_list(head):
    cur = head
    prev = None

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev


def display(head):
    while head:
        print(head.val)
        head = head.next


head = Node(1)
head.next = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)

new_head = reverse_linked_list(head)

print(display(new_head))
