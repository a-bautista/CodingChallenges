class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseList(head):
    current = head
    #nextNode = None
    previous = None

    while current:
        nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode

    return previous

    # prev = None
    # while head:
    #     curr = head
    #     head = head.next
    #     curr.next = prev
    #     prev = curr
    # return prev


def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    a.next = b
    b.next = c
    c.next = d
    d.next = None

    reverseList(a)
    print(d.next.value)
    print(c.next.value)
    print(b.next.value)


main()