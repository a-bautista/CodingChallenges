'''
    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

    Example:

    Input:
    [
        1->4->5,
        1->3->4,
        2->6
    ]
    Output: 1->1->2->3->4->4->5->6

'''

from typing import List

def main():

    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(5)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    head3 = ListNode(2)
    head3.next = ListNode(6)

    #
    # # [1,2,3,4]
    #
    # lkList2 = LinkedList()
    #
    # lkList2.head = ListNode(2)
    # node5 = ListNode(3)
    # node6 = ListNode(4)
    # node7 = ListNode(5)
    #
    # lkList2.head = node5
    # node5.next = node6
    # node6.next = node7
    #
    # #lkList1.printList()
    # #lkList2.printList()
    # #print([lkList1.printList(),lkList2.printList()])
    # #mergeLists([lkList1,lkList2])
    solution = Solution()
    res = solution.mergeKLists([head, head2, head3])
    print(res)

class ListNode:
    def __init__(self,val=0, next=None):
        self.val  = val
        self.next = next

class LinkedList:
    # initialize the linked list objects
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


'''Divide and conquer solution. Not my favorite, though.'''
# class SolutionDivideAndConquer:
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         amount = len(lists)
#         interval = 1
#         while interval < amount:
#             for i in range(0, amount - interval, interval * 2):
#                 lists[i] = self.merge2Lists(lists[i], lists[i + interval])
#             interval *= 2
#         return lists[0] if amount > 0 else lists
#
#     def merge2Lists(self, l1, l2):
#         head = point = ListNode(0)
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 point.next = l1
#                 l1 = l1.next
#             else:
#                 point.next = l2
#                 l2 = l1
#                 l1 = point.next.next
#             point = point.next
#         if not l1:
#             point.next=l2
#         else:
#             point.next=l1
#         return head.next

import heapq
def mergeKLists(lists):
    if len(lists) == 0:
        return None

    heap = [(lists[i].val, lists[i]) for i in range(len(lists)) if lists[i] is not None]
    heapq.heapify(heap)

    head, out = None, None

    while len(heap) > 0:
        x, n = heapq.heappop(heap)
        if out is None:
            out = ListNode(x)
            head = out
        else:
            out.next = ListNode(x)
            out = out.next

        if n.next is not None:
            heapq.heappush(heap, (n.next.val, n.next))
    return head


import queue
class Solution:

    def add_node_in_pq(self, idx, node, pq):
        #print(pq.queue)
        if node:
            pq.put((node.val, idx, node))

    def mergeKLists(self, lists):

        pq = queue.PriorityQueue()
        sorted_list_head = sorted_list_tail = ListNode(0)

        # add each node list in a priority Q
        for idx, node in enumerate(lists):
            self.add_node_in_pq(idx, node, pq)

        # start sorting them
        while not pq.empty():
            _, idx, node = pq.get()
            # get the next element of the priority queue
            self.add_node_in_pq(idx, node.next, pq)

            node.next = None
            sorted_list_tail.next = node
            sorted_list_tail = sorted_list_tail.next
        return sorted_list_head.next


# class SolutionMergeListsDefinitive:
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         lenlists = len(lists)
#         if lenlists == 0:
#             return lists
#
#         interval = 1
#         while interval < lenlists: # O(N)
#             for i in range(0, lenlists - interval, interval*2):  #O(N)
#                 lists[i] = self.mergelist(lists[i], lists[i+interval])
#             interval = interval*2
#
#         return lists[0]
#
#
#     def mergelist(self, l1, l2):
#         cur = dummy = ListNode(0)
#         while l1 and l2: #O(N)
#             if l1.val <= l2.val:
#                 cur.next = l1
#                 l1 = l1.next
#             else:
#                 cur.next = l2
#                 l2 = l2.next
#             cur = cur.next
#
#         cur.next = l1 or l2
#         return dummy.next

# brute force
def mergeKListsBruteForce(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    self.nodes = []
    head = point = ListNode(0) # initialize the head and point to a ListNode with value 0 which won't be displayed because the initial head value is not displayed in LinkedLists
    for l in lists:            # collect each list of lists
        while l:               # collect each element of each list
            self.nodes.append(l.val)
            l = l.next         # move on to the next element of the list
    for x in sorted(self.nodes):  # sort the list of values
        point.next = ListNode(x)  # convert each element into a Node
        point = point.next        # go on to the next element
    return head.next              # point and head started pointing to the same ListNode, point is pointing to the last node and head is pointing to the first element after the initial 0


if  __name__ == '__main__':
    main()
'''
    1->4->5,
    1->3->4,
    2->6
    
first 
elements 
    [(1, 0, [ 1, next: [ 4, next: [ 5, next: None]]]), 
     (1, 1, [ 1, next: [ 3, next: [ 4, next: None]]]), 
     (2, 2, [ 2, next: [ 6, next: None]])]
 
 
    [(1, 1, [ 1, next: [ 3, next: [ 4, next: None]]]), 
     (2, 2, [ 2, next: [ 6, next: None]]), 
     (4, 0, [ 4, next: [ 5, next: None]])]
 
 
    [(2, 2, [ 2, next: [ 6, next: None]]), 
     (4, 0, [ 4, next: [ 5, next: None]]), 
     (3, 1, [ 3, next: [ 4, next: None]])]
 
 
    [(3, 1, [ 3, next: [ 4, next: None]]), 
     (4, 0, [ 4, next: [ 5, next: None]]), 
     (6, 2, [ 6, next: None])]
 
 
    [(4, 0, [ 4, next: [ 5, next: None]]), 
    (6, 2, [ 6, next: None]), 
    (4, 1, [ 4, next: None])]
 
 
    [(4, 1, [ 4, next: None]), 
    (6, 2, [ 6, next: None]), 
    (5, 0, [ 5, next: None])]
 
 
    [(5, 0, [ 5, next: None]), 
    (6, 2, [ 6, next: None])]


    [(6, 2, [ 6, next: None])]

'''

'''
   For the MergeKLists solution, we can use the brute force approach where we collect each element of each list and we can sort
   each element in a ascending order. 
   
   The time complexity for this algorithm depends on collecting all elements from each list with nodes (O(N)), then if we pick
   a sorting algorithm, the worst case scenario will be O(n log(n)) and iterating through each node in the for loop costs O(N). 
   
   The complexity will be O(n log(n)). 
   
   The space complexity depends on the sorting that we choose, let's say we pick the Mergesort then the worst case will be O(N). 
   Creating a linked list costs O(N), so the space complexity is O(N).     
    
     
    solution to the priority Q
    The time complexity will be O (N log k) where k is the number of linked lists. We can merge two linked lists in O(n) time where n
    is the total number of nodes in two lists. If we sum up this process, we end up with O(N log k). 
    
    The space complexity will be 
    O(n) Creating a new linked list.
    O(k) The code above present applies in-place method which cost O(1) space. 
    And the priority queue (often implemented with heaps) costs O(k) space (it's far less than NNN in most situations). 
     
'''