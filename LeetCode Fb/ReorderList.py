'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

'''

class Solution:

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return
        a, b = self.splitList(head)
        b = self.reverseList(b)
        head = self.mergeLists(a, b)
        return head

    # Splits in place a list in two halves, the first half is >= in size than the second.
    # @return A tuple containing the heads of the two halves
    def splitList(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None
        return head, middle

    # Reverses only the second half of the list, not the first one
    # @return Returns the head of the new reversed list
    def reverseList(self, head):
        last = None
        currentNode = head
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = last
            last = currentNode
            currentNode = nextNode
        return last

    # Merges in place two lists
    # @return The newly merged list.
    def mergeLists(self, a, b):
        tail = a
        head = a
        a = a.next
        while b:
            tail.next = b # the magic happens here, the head which contains all the numbers gets affects
            tail = tail.next
            b = b.next
            if a:
                a, b = b, a
        return head


'''
    Time complexity: O(N)
    Space complexity: O(1)
'''