class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1:]

def main():

    q = Queue()
    q.enqueue(9)
    q.enqueue(10)
    q.enqueue("Theta")
    print(q.size())
    q.dequeue()
    print(q.peek())

main()