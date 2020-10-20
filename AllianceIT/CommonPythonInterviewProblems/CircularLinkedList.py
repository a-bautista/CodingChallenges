class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def circular_reference(LinkedList):
    # both pointers start in the same place
    fast, slow = LinkedList, LinkedList
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow==fast:
            return "Circular reference"
    return "Not a circular reference"

def main():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')

    a.next = b
    b.next = c
    c.next = d
    d.next = a # circular reference

    print(circular_reference(a))

main()

