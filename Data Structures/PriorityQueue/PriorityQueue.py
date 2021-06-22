'''

    Priority Queue is an extension of the queue with the following properties.
        An element with high priority (lowest number) is dequeued before an element with low priority (highest number).
        If two elements have the same priority, they are served according to their order in the queue.

    You can create the PriorityQueue with either queue.PriorityQueue or heapdict (an external module).

    PriorityQueue
    Functions:
        put() – Puts an item into the queue.
        get() – Removes and returns an item from the queue.
        qsize() – Returns the current queue size.
        empty() – Returns True if the queue is empty, False otherwise. It is equivalent to qsize()==0.
        full() – Returns True if the queue is full, False otherwise. It is equivalent to qsize()>=maxsize.

    Heapdict implements the MutableMapping ABC, meaning it works pretty much like a regular Python dictionary.
    It’s designed to be used as a priority queue. Along with functions provided by ordinary dict(), it also has popitem()
    and peekitem() functions which return the pair with the lowest priority. Unlike heapq module, the HeapDict supports
    efficiently changing the priority of an existing object (“decrease-key” ).
    In the Heapdict, the value with the highest priority contains the highest value.

    Functions:
        clear(self) – D.clear() -> None. Remove all items from D.
        peekitem(self) – D.peekitem() -> (k, v), return the (key, value) pair with lowest value; but raise KeyError if D is empty.
        popitem(self) – D.popitem() -> (k, v), remove and return the (key, value) pair with lowest value; but raise KeyError if D is empty.
        get(self, key, default=None) – D.get(k[, d]) -> D[k] if k in D, else d. d defaults to None.
        items(self) – D.items() -> a set-like object providing a view on D’s items
        keys(self) – D.keys() -> a set-like object providing a view on D’s keys
        values(self) – D.values() -> an object providing a view on D’s values


    Time complexity;
        peek 	 O(1) # check the element with the highest priority
        dequeue  O(lg(n))
        enqueue  O(lg(n))

    Space complexity:
        space 	 O(n)

'''

from queue import PriorityQueue
#import heapdict # this package was installed because it wasn't included in Python modules

def main():

    q = PriorityQueue()
    #q2 = heapdict.heapdict()

    q.put((2,'g'))
    q.put((4,'h'))
    q.put((1,'t'))
    q.put((10,'h'))
    q.put((3,'jiu'))

    # q2['h'] = 20
    # q2['u'] = 1
    # q2['w'] = 3

    print('Print all the elements in the Priority Q:')
    print(q.queue)

    print('Removing the values with the highest priority')
    print(q.get())
    print('Removing the values with the highest priority')
    print(q.get())


    print('Print all the elements in the Priority Q:')
    print(q.queue)

    # print('\nImplementation of the Priority Q with heapdict')
    # print('List of key:value pairs in h:\n', list(q2.items()))

    # print('value with the lowest priority:', q2.peekitem())
    # print('Removing the value with the lowest priority\n')


    # q2.popitem()
    # print('list of key:value pairs in h:\n',
    #       list(q2.items()))

    #print(q2.get())


if __name__ == '__main__':
    main()
