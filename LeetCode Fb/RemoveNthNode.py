'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head, n):
    # Create a dummy LinkedList node
    dummy = ListNode(0)
    # Point the dummy linked list to the head
    dummy.next = head
    # Make two more pointers which will point to dummy (we are making the values to be the same as dummy)
    fast = slow = dummy

    #Skip N nodes from the fast linkedlist
    for _ in range(n):
        fast = fast.next

    # Start advancing 1 node until fast only contains 1 node
    # This causes the slow pointer to stop in the Nth node to be removed
    while fast and fast.next:
        fast = fast.next
        slow = slow.next

    # Skip the Nth node by disconnecting it. The slow.next will point to the next.next node (so you skip the Nth node)
    slow.next = slow.next.next
    # dummy is a copy of slow, so dummy will be affected by the line from above
    return dummy.next


'''
    Time complexity: O(L)
    Space complexity: O(1)
'''