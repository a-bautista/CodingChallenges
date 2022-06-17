def product_self_array(nums):
    res = [1 for _ in nums]
    left = 1
    right =1
    for i in range(len(nums)):
        # update the left part of the array
        # in the first pass you will multiply teh first and last values of the array but this is
        # expected because we multiply these values by 1, then we get the next value of the arrays
        # with the pointers
        res[i]*= left
        res[-1-i]*=right
        
        # update the pointers with the values from the array, then on the next round the res array
        # will contain the results of multiplication except self
        left*=nums[i]
        right*=nums[-1-i]
    return res


def main():
    nums = [1, 2, 3]
    res = product_self_array(nums)
    print(res)

main()