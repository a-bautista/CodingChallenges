'''
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

    Example 1:

    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
    2 is the missing number in the range since it does not appear in nums.
    Example 2:

    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
    2 is the missing number in the range since it does not appear in nums.

    Solution 1: HashMap

    nums = [1,4,5]

    Create a hashmap, so you will have the following data structure:

    {
        1:1,
        4:1,
        5:1
    }

    Instead of using a max(set(list(nums))) to get the max value in the array, you
    can use the len(nums)+1 because you get the missing elements

    Time complexity: O(N)
    Space complexity: O(N)

    --------------------------------------------------------------------------


'''

def sol_hash_map(nums):
    hash_map = dict()
    result = []
    #max_val = max(list(set(nums)))

    for n in nums:
        if n not in hash_map:            
            hash_map[n]=1

    #for n in range(1, max_val):
    for n in range(1, len(nums)+1):
        if n not in hash_map:
            result.append(n)
    return result


def main():
    nums = [4,3,2,7,8,2,3,1]
    nums2 = [1,4,5]
    sol = sol_hash_map(nums2)

    print(sol)


main()