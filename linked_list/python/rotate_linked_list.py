class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def display_list(head):
    while head:
        print(head.val)
        head = head.next


def rotate_linked_list(head, k):
    last = head

    length = 1

    while last.next:
        last = last.next
        length += 1

    k = k % length

    last.next = head

    for _ in range(length-k-1):
        head = head.next

    ans = head.next
    head.next = None

    return ans


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

# print(rotate_linked_list(head, 4))

new_head = rotate_linked_list(head, 4)
print(display_list(new_head))
