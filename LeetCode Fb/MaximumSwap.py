"""
    Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
    Return the maximum valued number you could get.
    Example 1:

    Input: 2736
    Output: 7236
    Explanation: Swap the number 2 and the number 7.

"""

class Solution:
    def maximumSwap(self, num):
        # convert the num into a list, so you can iterate through each number
        A = list(str(num))
        # display the index of each element but notice that this is a set
        # so, you will only see the indexes of the different numbers
        last = {int(x): i for i, x in enumerate(A)}
        # enumerate each element of the list 0:1, 1:7, 2:7, 3:7
        for i, x in enumerate(A):
            # start in 9, stop at int(x) and subtract 1, we use 9 because we have 9 values from 1-9
            for d in range(9, int(x), -1):
                # if there's an element 'd' in the set that is greater than the current index i then replace it
                # by doing a swap. The get(d,0) indicates to get the numeric value. 
                if last.get(d,0) > i:
                    # do the swap
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(A))
        return num

def main():
    #num = 2273
    num = 2003
    solution = Solution()
    res = solution.maximumSwap(num)
    print(res)

main()