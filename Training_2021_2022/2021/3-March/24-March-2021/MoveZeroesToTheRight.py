'''
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Example 1:

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Example 2:

    Input: nums = [0]
    Output: [0]

'''

def solve(nums):
    write = read = 0
    while read < len(nums):
        if nums[read]!=0:
            nums[read], nums[write] = nums[write], nums[read]
            write+=1
        read+=1
    
    while write< len(nums):
        nums[write] = 0
        write+=1

def main():
    nums = [0,1,0,3,12]
    solve(nums)
    print(nums)

main()

