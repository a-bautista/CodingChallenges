def hasCycle(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

'''
    Tortoise and hare problem, we are trying to see if slow catches up to the fast pointer and if so, then we say we have
    a linkedlist cycle. 
    
    Time complexity: O(N)
    Space complexity: O(1)
'''