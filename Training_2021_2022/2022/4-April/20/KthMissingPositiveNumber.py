'''
    Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

    Find the kth positive integer that is missing from this array.

    Example 1:

    

'''

def findKthPositive(a, k):
    l, r = 0, len(a)
    while l < r:
        mid = l +(r- l) // 2
        if a[mid] - mid > k:
            r = mid
        else:
            l = mid + 1
    return r + k 

def main():

    arr = [2,3,4,7,11]
    k = 5

    res = findKthPositive(arr, k)
    print(res)

main()
