'''
    Given an array of numbers which is sorted in ascending order and also rotated by some 
    arbitrary number, find if a given ‘key’ is present in it.

    Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. 
    You can assume that the given array does not have any duplicates.

    Example 1:

    Input: [10, 15, 1, 3, 8], key = 15
    Output: 1
    Explanation: '15' is present in the array at index '1'.
    
    Linear search is not accepted, you must use binary search.

'''
def solve_binary_search(nums, target):
    start = 0
    end = len(nums)-1

    while start<=end:
        mid = start + (end - start)//2

        # Case I: target at the middle
        if nums[mid] == target:
            return mid

        # Case II: Focus in the numbers that are less than the mid
        if nums[start]<=nums[mid]:
            # the target is between the start and middle number          
            if target >= nums[start] and target < nums[mid]:
                # disregard the right side
                end = mid - 1
            # the target is not in the left side
            else:
                #  disregard the left side
                start = mid + 1  
        
        # Case III. Focus in the numbers greater than mid
        else:
            # the target is between the middle number and the end of the array
            if target >= nums[mid] and target < nums[end]:
                # disregard the left side
                start = mid + 1

            else:
                # disregard the right side 
                end = mid -1 
    return -1

def main():
    print(solve_binary_search([10, 15, 1, 3, 8], 15))
    print(solve_binary_search([4, 5, 7, 9, 10, -1, 2], 10))

main()
  



        # Case III: target is below mid point
        

        