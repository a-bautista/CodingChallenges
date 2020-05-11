
'''
    The property of this data structure in python is that each time the smallest of heap element is popped(min heap).
    Whenever elements are pushed or popped, heap structure in maintained. The heap[0] element also returns the smallest element each time.
    The heap structure is maintaining the elements sorted in a binary tree structure and inserting values in pre-order.

    Operations on heap :
        1. heapify(iterable) :- This function is used to convert the iterable into a heap data structure. i.e. in heap order.
        2. heappush(heap, ele) :- This function is used to insert the element mentioned in its arguments into heap. The order is adjusted, so as heap structure is maintained.
        3. heappop(heap) :- This function is used to remove and return the smallest element from heap. The order is adjusted, so as heap structure is maintained.

    A min-heap has the smallest value at the top. A max-heap has the largest value at the top. We'll describe min-heaps
    here, but the implementation for max-heaps is nearly identical.

    Time complexity:
        get min 	O(1)
        get max     O(1)
        remove min 	O(lg(n))
        insert 	    O(lg(n))
        heapify 	O(n) # converts a list into a heap

    Space complexity:
        space 	O(n)
'''

import heapq

def main():
    # Python code to demonstrate working of
    # nlargest() and nsmallest()

    # initializing list
    li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

    # using heapify() to convert list into heap
    heapq.heapify(li1)

    print('The heap is displayed in a new arranged order:')
    print(list(li1))

    # using nlargest to print 3 largest numbers
    print("The 2 largest numbers in list are : ", end="")
    print(heapq.nlargest(2, li1))

    # using nsmallest to print 3 smallest numbers
    print("The 2 smallest numbers in list are : ", end="")
    print(heapq.nsmallest(2, li1))

    # add a new element to the heap and keep the order of the heap
    print('Added element 89 to the heap ')
    heapq.heappush(li1,89)
    print(list(li1))

    # remove the element with the lowest value, in this case element 1
    print('Remove the lowest element from the heap')
    heapq.heappop(li1)
    print(list(li1))

    # heapreplace() removes the lowest element and the pushed element can take its place as the lowest element if it is lower than the popped element
    print("The popped item using heapreplace() is : ", end="") # element 3 is removed
    print(heapq.heapreplace(li1, 7))
    print(list(li1))

    # heapq.heappushpop() pushes the new element and then it removes the lowest element at the same time.
    print("The pushpopped item using heap.pushpop is: ", end="")
    print(heapq.heappushpop(li1,9))
    print(list(li1))


if __name__ == '__main__':
    main()