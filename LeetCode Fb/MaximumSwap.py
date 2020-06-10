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
        A = list(str(num))
        # display the index of each element but notice that this is a set
        # so, you will only see the indexes of the different numbers
        last = {int(x): i for i, x in enumerate(A)}
        # enumerate each element of the list 0:1, 1:7, 2:7, 3:7
        for i, x in enumerate(A):
            # subtract with range(9, int(x),-1)
            for d in range(9, int(x), -1):
                # if there's an element 'd' in the set which is replaced
                # at position 0 and is greater than i then do the swap
                if last.get(d, 0) > i:
                    # do the swap
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(A))
        return num

def main():
    number = 1777 # 7173 -> 7713
    number2 = 2736
    solution = Solution()
    result = solution.maximumSwap(number2)
    print(result)

main()