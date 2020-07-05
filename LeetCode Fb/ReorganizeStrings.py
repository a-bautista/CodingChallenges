
from collections import Counter
import heapq

def reorganizeString(S):
    res, c = [], Counter(S)
    # build a list to store the values in a negative format
    # we will use this for simulating a max heap with negative values
    pq = [(-value ,key) for key ,value in c.items()]

    # convert the heap into a max heap (in essence this is a min heap because
    # the lowest value is at the top but because of this then we know that
    # if we remove the negative elements we will have our list with always top values
    heapq.heapify(pq)

    # these variables will work to store the previous letter and previous value
    previous_count, previous_value = 0, ''
    while pq:
        # pop the element which is at the top of the heap
        current_count, current_val = heapq.heappop(pq)

        # add the value from the heap to the list
        res.append(current_val)

        # we add the previous count and value because we need them back
        # in our heap to indicate that we still have elements to add to the list
        if previous_count < 0:
            heapq.heappush(pq, (previous_count, previous_value))

        # use this variable to decrease the count number
        current_count += 1

        previous_count, previous_value = current_count, current_val

    res = ''.join(res)
    if len(res) != len(S):
        return ""

    return res

def main():
    s = 'aab'
    res = reorganizeString(s)
    print(res)

main()

'''
    Time complexity: O(N*Log(A)) where A is the # of alphabet letters.
    However, because we remove and add back elements to the heap and we only
    add 1 character to the result at each iteration then there will be N*Log(A) call
    or N iterations * 26 (the size of the alphabet). Thus this is O(N)
    Space complexity: O(A) 
'''