'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are
not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""

Note:

    S will consist of lowercase letters and have length in range [1, 500].

'''

# solution: Greedy + Heap
from collections import Counter
import heapq

def reorganizeString(S):
    # Get the count of all the elements in the given string
    res, c = [], Counter(S)

    # build a list to store the values in a negative format
    # we will use this for simulating a max heap with negative values
    # pq =[(-2,'a'),(-1,'b')]
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

        # add the value from the heap to the list result
        res.append(current_val)

        # we add the previous count and value because we need them back
        # in our heap to indicate that we still have elements to add to the list
        if previous_count < 0:
            heapq.heappush(pq, (previous_count, previous_value))

        # use this variable to decrease the count number of the letter to simulate that we have one letter less
        current_count += 1

        previous_count, previous_value = current_count, current_val

    res = ''.join(res)
    # if the len of the result is not the same as the given string then it is not possible to reorganize the string
    if len(res) != len(S):
        return ""

    return res

def main():
    s = 'aaba'
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