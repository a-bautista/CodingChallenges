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