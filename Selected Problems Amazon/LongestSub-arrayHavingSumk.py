'''

Given an array arr[] of size n containing integers. The problem is to find the length of the longest sub-array having
sum equal to the given value k.

Input : arr[] = { 10, 5, 2, 7, 1, 9 },
            k = 15
Output : 4

The sub-array is {5, 2, 7, 1}.

Input : arr[] = {-5, 8, -14, 2, 4, 12},
            k = -5
Output : 5

Requirements:

    1. array < k return an error
    2. What if there's not any sum that throws 15? do I return an error?


    Naive approach
    index  value   sum
    0     : 10     = 10 (i+0)
    1     : 10 + 5 = 15 (i+1) value found, reset i = index where the value was found and len of value = 2
    2     : 5      =  5 (i+0)
    3     : 5+2    =  7 (i+1)
    4     : 5+2+7   = 14  (i+2)
    5     : 5+2+7+1 = 15  (i+3) value found, reset i = index where the value was found and len of value = 4

    The problem with this approach is that I am using two loops and this will cause an O(n**2) time complexity.
    I think I can keep this in a O(n) approach with only 1 loop and storing the values in a hash map.
'''

def lenOfLongSubarr(arr, n, k):
    # dictionary mydict implemented
    # as hash map
    mydict = dict()

    # Initialize sum and maxLen with 0
    sum = 0
    maxLen = 0

    # traverse the given array
    for i in range(n):

        #print(mydict)
        # accumulate the sum
        sum += arr[i]
        #print(sum)

        # when subArray starts from index '0' and I found the value at index 0
        if (sum == k):
            maxLen = i + 1

        # check if 'sum-k' is present in
        # mydict or not


        elif (sum - k) in mydict:
            #print('Sum - K')
            #print(maxLen)
            maxLen = max(maxLen, i - mydict[sum - k])
            #print('New Max Len')
            #print(maxLen)

            # if sum is not present in dictionary
        # push it in the dictionary with its index
        if sum not in mydict:
            mydict[sum] = i

        #print('Max Len values')
        #print(maxLen)
    return maxLen

class Solution:
    def maxSubArrayLen(self, nums, k):
        ans, sum = 0, 0               # answer and the accumulative value of nums
        mp = {0:-1}                 #key is acc value, and value is the index
        for i in range(len(nums)):
            sum += nums[i]
            if sum not in mp:
                mp[sum] = i
            if sum-k in mp:
                ans = max(ans, i-mp[sum-k])
        return ans

"""
    where k = 9 and n = [2, 8, 1, 7, 13]
    index  sum  sum -k
    0       2    2 - 9 = -7
    1       10   10 - 9 = 1
    2       11   11 - 9 = 2
    3       18   18 - 9 = 9
    4       19   19 - 9 = 10
    5       22   22 - 9 = 13
    
    max(ans, index - mydict[sum-k])
    max(0, 2 - mydict[11-9]=2 and 2 (sum) is mapped to index 0)
    max(0, 2- 0)
    max(0, 2)
    
    max(0, 4 - mydict[10]=1 and 10 (sum) is mapped to index 1)
    max(2, 4-1)
    max(2, 3)
    
"""


# Driver Code
if __name__ == '__main__':
    arr = [2, 8, 1, 7, 1, 3]
    n = len(arr)
    k = 9
    #print("Length =", lenOfLongSubarr(arr, n, k))
    solution = Solution.maxSubArrayLen(Solution, arr,9)
    print(solution)