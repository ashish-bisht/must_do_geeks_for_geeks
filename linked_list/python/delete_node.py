class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def delete_node(head, to_delete):
    cur = dummy = Node("X")
    cur.next = head
    while cur and cur.next:
        if cur.next.val == to_delete:
            cur.next = cur.next.next
            break
        cur = cur.next
    return dummy.next


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

new_head = delete_node(head, 3)

print(display(new_head))


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

new_head = delete_node(head, 1)

print(display(new_head))

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

new_head = delete_node(head, 6)

print(display(new_head))
