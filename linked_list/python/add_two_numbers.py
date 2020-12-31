class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_two_numbers(head1, head2):
    new_list = dummy = Node("X")
    carry = 0
    total = 0
    while head1 or head2:
        cur1, cur2 = 0, 0
        if head1:
            cur1 = head1.val
            head1 = head1.next
        if head2:
            cur2 = head2.val
            head2 = head2.next

        total = (cur1 + cur2 + carry) % 10
        carry = (cur1 + cur2 + carry) // 10
        dummy.next = Node(total)
        dummy = dummy.next

    if carry == 1:
        dummy.next = Node(carry)
    return new_list.next


def display(head):
    while head:
        print(head.val)
        head = head.next


head1 = Node(2)
head1.next = Node(4)
head1.next.next = Node(3)

head2 = Node(5)
head2.next = Node(6)
head2.next.next = Node(4)

new_head = add_two_numbers(head1, head2)
print(display(new_head))
