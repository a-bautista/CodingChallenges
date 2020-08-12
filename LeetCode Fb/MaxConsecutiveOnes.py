'''
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.



Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


'''

def longestOnes(A, K):
    left = 0

    for right in range(len(A)):
        # When you find a zero then decrease the value of K
        K -= 1 - A[right]
        # When you have a negative K then it means you are not allowed to increase the 
        # window from the right, so increase from the left to maintain the window of zeroes 
        # under the value of K
        if K < 0:
            K += 1 - A[left]
            left += 1
    return right - left + 1

def main():
    A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    K = 2
    res = longestOnes(A,K)
    print(res)

main()

'''
    Time complexity: O(N)
    Space complexity: O(1)
'''