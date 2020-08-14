'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

1. Find the middle linkedlist
2. Divide the middle number into two linkedlist and sort each
3. Merge the linkedlist in the right order

Reduce the linkedlist by half with the two pointer approach
slow and fast pointer

 -1 ->  5 -> 3  -> 4  ->  0
        ^    ^            ^
       prev slow         fast


so prev is the first half
prev.next = None (disregard what's next)
second half is from slow to fast.

-1 -> 5 -> 3
^

3 -> 4 -> 0
^


-1<3 yes, then
-1->
move the pointer from the first list

-1 -> 5 -> 3
      ^

3 -> 4 -> 0
^



5<3, No, then
-1->3
move the pointer from the second list


'''


class Solution(object):
    def merge(self, left, right):
        # dummy keeps track of the list which contains the sorted elements
        dummy = tail = ListNode(None)
        while left and right:
            if left.val < right.val:
                tail.next, left = left, left.next
            else:
                tail.next, right = right, right.next
            tail = tail.next

        tail.next = left or right
        return dummy.next
    # this divides the list by the middle
    def sortList(self, head):
        # base case
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head

        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        # set the first half to left
        left = self.sortList(head)

        # set the second half to right
        right = self.sortList(slow)

        # merge results
        return self.merge(left, right)

        #return self.merge(*map(self.sortList, (head, slow)))