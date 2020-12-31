class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_in_group(head, k):


def display(head):
    while head:
        print(head.val)
        head = head.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

new_head = reverse_in_group(head, k)
print(display(head))
