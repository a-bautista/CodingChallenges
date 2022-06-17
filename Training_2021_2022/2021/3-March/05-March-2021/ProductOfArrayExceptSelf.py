'''
    input: nums = [2,3,4,5]
    output: nums = [60, 40, 30, 24]

    left  = 1
    right = 1

    for i in range(len(nums))
       # update the values in the array, the first time the values will be multiplied by 1
        nums[i]*=left
        left[-1-i]*=right
        
        # move the pointers and carry the numbers that you had already 
        left*=nums[i]
        right*=nums[-1-i]
    
    return nums

    This is not an in-place solution
'''

def solve(nums):
    # create an array which will contain the results
    res = [1 for _ in range(len(nums))]

    # the pointers are carrying the multiplied values
    left  = 1
    right = 1

    for i in range(len(nums)):
       # update the values in the new array, the first time the values will be multiplied by 1
       # # multiply the current value in the array with the carried value in the pointer
        res[i]*=left
        res[-1-i]*=right
        
        # move the pointers and carry the numbers that you had already 
        left*=nums[i]
        right*=nums[-1-i]
    
    return res

def main():
    nums = [2,3,4,5]
    res = solve(nums)
    print(res)

main()