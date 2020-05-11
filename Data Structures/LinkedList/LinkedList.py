'''

    Head -> A | next -> B | next -> C | next -> D | NULL


    Three nodes have been created.
    We have references to these three blocks as head,
    second and third

    lkList.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+


    Now next of second Node refers to third.  So all three
    nodes are linked.

    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+

'''

def main():
    lkList      = LinkedList()
    lkList.head = Node(1)
    secondNode  = Node(2)
    thirdNode   = Node(3)

    lkList.head.next = secondNode
    secondNode.next = thirdNode
    lkList.printList()



class Node:
    def __init__(self, data):
        self.data = data  # assign data
        self.next = None  # initialize next as Null


class LinkedList:
    # initialize the linked list objects
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    main()

