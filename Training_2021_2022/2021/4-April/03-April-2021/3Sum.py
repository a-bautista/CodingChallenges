'''
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
    and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Example 2:

    Input: nums = []
    Output: []

    Example 3:

    Input: nums = [0]
    Output: []

    There's a two pointers technique + one additional pointer which will start from the leftPointer + 1

'''

def solve(nums):
    res = [] # this variable will hold the results
    # 1. Start by sorting the array in ascending order
    nums.sort()

    # 2. Start a for loop with range(len(nums)-2)
    for i in range(len(nums)-2):

        # edge case: repeated values such as [-1,1,0,-1,1,0,-1,1,0]
        if i>0 and nums[i]==nums[i-1]:
            continue
        # 3. Initialize your pointers left and right (notice that left starts at i + 1 and not at 0 because i will be
        # the other pointer)
        left  = i + 1
        right = len(nums)-1

        while left<right:
        
            # 4. Get the sum of the 3 pointers
            currentSum = nums[left] + nums[right] + nums[i]

            # 5. Start a sort of binary search where you increment the left or decrement the right pointer
            if currentSum > 0:
                right -=1
            elif currentSum < 0:
                left +=1
            # 6. Set the logic when you have found a 0, i.e., append the value and increae the pointers
            else:
                res.append([nums[left],nums[right], nums[i]])
                
                # edge case avoid counting the values you have already considered into the array, i.e., [-1,1,0,-1,1,0,-1,1,0]
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1
                left +=1
                right-=1
    return res

def main():
    nums = [-1, 0, 1, 2, -1, -4]
    res = solve(nums)
    print(res)

main()

