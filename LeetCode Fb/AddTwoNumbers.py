"""
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
    order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

    2->4->3

    5->6->4
       ^

    curr.res-->7->0->8
    suma contains the 1 that will be added to the very last node



"""
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        suma = 0

        while l1 or l2 or suma:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            suma, out = divmod(val1 + val2 + suma, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


def addTwoNumbers(self, l1, l2):
    # create the dummy head which will point to the result
    dummy = cur_res = ListNode(0)

    # use the suma list to hold the sum of values
    suma = 0
    # while we have values to point in the lists, sum the values of l1.val and l2.val and add them to suma.
    # go onto the next node for each list

    while l1 or l2 or suma:
        if l1:
            suma += l1.val
            l1 = l1.next
        if l2:
            suma += l2.val
            l2 = l2.next
        
        # suma%10 contains the result of the sum without the carry
        cur_res.next = ListNode(suma%10)

        # go onto the next node in the list
        cur_res = cur_res.next
        # suma // = 10 contains the carried value that needs to be added next
        suma //= 10
    return dummy.next


'''
    Time complexity: O(max(M,N))
    Space complexity: O(max(M,N))
'''