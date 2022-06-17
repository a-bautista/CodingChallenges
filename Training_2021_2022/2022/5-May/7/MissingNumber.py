'''
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


    3 solutions:
    
    1. Gaus Formula:
        
        (n * (n + 1) / 2)

        You need to sum all the numbers from the array and then subtract the current 
        sum of the array and that will give you the missing number.
        
        Time complexity: O(n)
        Space complexity: O(1)
    
    2. HashSet

        Time complexity: O(n)
        Space complexity: O(n)

    3. Bit manipulation

        Time complexity: O(n)
        Space complexity: O(1)

        Example of how bit manipluation works.

        [0,1,3]

        missing = len(nums)

        for i, num in enumerate(nums):

            missing ^= i ^ num

        return missing

        missing = 3
        i       = 0
        num     = 0

        We cancel missing and num because they have the same value.
        
        missing = 3
        i = 1
        num = 1

        missing = 3
        i = 2
        num = 2

        missing = 2
'''

def missing_number_gaus(nums):
    len_n = len(nums)
    return (len_n * (len_n + 1) / 2) - sum(nums)


def hash_set(nums):
    set_nums = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in set_nums:
            return number

def bitwise(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


def main():
    nums = [9,6,4,2,3,5,7,0,1]
    nums2 = [0,1,3]
    
    sol_gaus = missing_number_gaus(nums)
    print(sol_gaus)

    sol_hash = hash_set(nums)
    print(sol_hash)

    sol_bitwise = bitwise(nums2)
    print(sol_bitwise)

main()