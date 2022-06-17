"""
    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
    the non-zero elements.

    Example:

    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.



"""

def solve(nums):

    if len(set(nums))<1:
        return -1

    # record the position of 0
    start = 0
    for i in range(len(nums)):
        
        if nums[i] == 0: 
            #nums[i], nums[zero] = nums[zero], nums[i]
            holder = nums[start:i]
            nums[start] = 0
            nums[start + 1:i] = holder
            start+=1
    return nums

def main():
    nums  = [0,1,0,3,12]
    nums2 = [1, 10, -1, 11, 5, 0, -7, 0, 25, -35]
    res = solve(nums2)
    print(res)

main()
