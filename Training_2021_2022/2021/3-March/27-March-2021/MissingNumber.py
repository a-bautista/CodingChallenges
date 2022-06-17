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

'''
    Solution: 
        O(n) time complexity
        O(n) space complexity
'''
def solve(nums):
    setNums = set(nums)
    for i in range(len(nums)):
        if i not in setNums:
            print(i)

'''
    Gauss Formula:
        Get sum of len(nums) with (n*(n+1))//2 (Gauss Sum)
        Subtract the Gauss sum - the sum of the elements that we have in the array
        Time complexity: O(N)
        Space complexity: O(1)
'''
def solveGauss(nums):
    n = len(nums)
    gaussSum = (n*(n+1))//2
    suma = sum(nums)
    return gaussSum - suma

def main():
    nums = [3,0,1]
    solve(nums)
    res = solveGauss(nums)
    print(res)

main()