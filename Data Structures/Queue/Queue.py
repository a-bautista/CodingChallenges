'''

A queue stores items in a first-in, first-out (FIFO) order.
A queue works like in the line of a restaurant. First come, first served.

Queue in Python can be implemented using deque class from the collections module. Deque is preferred over list in the
cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time
complexity for append and pop operations as compared.

Queues can be created from the deque class from the collections module or from the Python built in module queue.Queue

Time complexity:
    enqueue  O(1)
    dequeue  O(1)
    peek 	 O(1)

Space complexity:
    space 	 O(n)

'''

from collections import deque

def main():
    q = deque()
    q.append(5)
    q.append(9)
    q.append(4)

    print(q.__len__())
    print(q)

    # this method is how truly the queue removes an element, 5 was inserted first and it needs to be removed
    q.popleft()
    print(q)

    q.pop()
    print(q)



if __name__ == '__main__':
    main()
