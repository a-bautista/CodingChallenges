class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

def return_nth_node(node, value):
    left_pointer  = node
    right_pointer = node

    for _ in range(value-1):
        # Edge case: None value
        if not right_pointer.next:
            raise LookupError('Error: ')

        right_pointer = right_pointer.next

    while right_pointer.next:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    return left_pointer.value

def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    res = return_nth_node(a, 3)
    print(res)

main()