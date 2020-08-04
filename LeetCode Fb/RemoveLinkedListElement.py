
'''
    Remove all elements from a linked list of integers that have value val.

    Example:

    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5

'''

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next

'''
    Time complexity: O(N)
    Space complexity: O(1)
'''