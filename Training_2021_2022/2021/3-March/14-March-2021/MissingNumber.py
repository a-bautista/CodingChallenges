'''
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing 
    from the array.

    Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range 
    since it does not appear in nums.

    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range 
    since it does not appear in nums.

'''

def solve(nums):
    '''
        Time complexity: O(N)
        Space complexity: O(N)
    '''
    numSet = set(nums)
    n = len(nums)+1
    for i in range(n):
        if i not in numSet:
            return i
    # if i is contained in all numbers from numSet then no need to return
    return 

def solve_gauss(nums):
    '''
        Gauss Formula: (n*(n+1))/2
        Return the the sum of Gauss formula - the sum of nums
        Time complexity: O(N)
        Space complexity: O(1)
    '''
    gauss = len(nums)*(len(nums)+1)//2
    n = sum(nums)
    return gauss - n


def main():
    nums = [0,1,3]
    res = solve(nums)
    res2 = solve_gauss(nums)
    # print(res)
    print(res2)

main()    

