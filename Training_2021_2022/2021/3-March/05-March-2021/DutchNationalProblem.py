'''

Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects,
hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of
three different numbers that is why it is called Dutch National Flag problem.

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

[1, 0, 2, 1, 0]
 ^           ^

 low = 0
 high = len(nums)-1

 for i in range(len(nums)):
     if nums[i] == 0:
         nums[i], nums[low] = nums[low], nums[i]
         low+=1
     elif nums[i] == 2:
         nums[i], nums[high] = nums[high], nums[i]
         high-=1


 while left < = right:
     if nums[left] == 0:
         nums[left], nums[right] = nums[right], nums[left]
         
We have 3 pointers: low, high and current index
'''

def solve(nums):
    current = low = 0
    high = len(nums)-1
    
    while current<=high:
        if nums[current]==0:
            nums[current], nums[low] = nums[low], nums[current]
            low+=1
            current+=1
        elif nums[current]==1:
            current+=1
        else:
            # you found a value of 2
            nums[high], nums[current] = nums[current], nums[high]
            high-=1
    return nums

def main():
    nums = [1, 0, 2, 1, 0]
    print(solve(nums))

main()