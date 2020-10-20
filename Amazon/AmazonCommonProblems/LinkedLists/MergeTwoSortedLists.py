

def main():
    l1node1 = ListNode(1)
    l1node2 = ListNode(4)
    l1node3 = ListNode(5)

    l1node1.next = l1node2
    l1node2.next = l1node3
    l1node3.next = None

    l2node1 = ListNode(1)
    l2node2 = ListNode(2)
    l2node3 = ListNode(3)
    l2node4 = ListNode(6)

    l2node1.next = l2node2
    l2node2.next = l2node3
    l2node4.next = None

    l1 = []
    l2 = []

    l1.append(l1node1)
    l1.append(l1node2)
    l1.append(l1node3)

    l2.append(l2node1)
    l2.append(l2node2)
    l2.append(l2node3)
    l2.append(l2node4)

    for val in l1:
        print(val.val)

    for val in l2:
        print(val.val)

    #solution = Solution.mergeTwoLists(Solution, l1, l2)
    #print(solution)


class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next


class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

if __name__ == '__main__':
    main()

'''
    
    Problem definition:
    
    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
    
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
    
    Proposed Solution: Iteration
    Time complexity : O(n+m)

    Because exactly one of l1 and l2 is incremented on each loop iteration, the while loop runs for a number of iterations equal 
    to the sum of the lengths of the two lists. All other work is constant, so the overall complexity is linear.

    Space complexity : O(1)

    The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.

'''
