class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.next = b
    b.next = c
    print("This is the value of the node A: "+str(a.value))
    print("This is the value of the node B: "+str(a.next.value))

main()