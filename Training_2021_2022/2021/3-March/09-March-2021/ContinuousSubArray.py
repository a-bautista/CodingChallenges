"""
    Given a list of non-negative numbers and a target integer k, write a function to check if the array has a
    continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n
     is also an integer.

     Input: [23, 2, 4, 6, 7],  k=6
     Output: True
     Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

     Input: [23, 2, 6, 4, 7],  k=42
     Output: True
     Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

     The approach to follow is an accumulative sum % k

     {0:0, 5:1, 1:2}

     The first numbers store the values of the cumulative sum % K and if we see
     The second numbers are the indexes of i when you enumerated the array.
     The approach is that if we see a value in the cache and if the next value in the cache is greater than the
     index then it means that we have found numbers that sum equal to k.

"""
def solve(nums, k):
    current = 0
    dp = {}
    for i, value in enumerate(nums):
        
        if current not in dp:
            dp[current] = i
        # ( current + x ) % k is the accumulative sum but % k will indicate a previous existence 
        # we use the modulo % because we are tied to the contiguous number of elements in the array
        current = (current+value)%k if k!=0 else current + value
        # if we have seen the current value before in the dictionary then this means that we do not need to 
        # traverse the entire array because there's a previous value from the % operation
        if current in dp:
            return True
    return False

def main():
    nums = [23, 2, 4, 6, 7]
    k = 2
    res = solve(nums, k)
    print(res)

main()
