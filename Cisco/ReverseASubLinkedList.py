'''
    Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse
    the LinkedList from position ‘p’ to ‘q’.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def iterate_linkedlist(node, p, q):

    
    while node:

        print(node.value)
        node = node.next


def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    iterate_linkedlist(a, 2, 4)



main()
