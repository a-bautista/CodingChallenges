class DoubleLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def main():
    a = DoubleLinkedList(10)
    b = DoubleLinkedList(5)
    c = DoubleLinkedList(15)

    a.next = b
    b.prev = a

    b.next = c
    c.prev = a
    
main()