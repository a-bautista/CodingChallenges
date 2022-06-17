'''
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
    such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
    (0-indexed). 
                        
    
    For example, given nums = [0,1,2,4,5,6,7] but once we rotate it then we get [4,5,6,7,0,1,2] and given the target 0
    then we need to return its index position which is 4.

    target = 0
    nums   = [4,5,6,7,0,1,2]
              0 1 2 3 4 5 6
    return 4 because that's the index of 0

    nums = [4,5,6,7,0,1,2], target = 3
    return -1 because there's not any 3 in the array

'''

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                # return the index of the array
                return mid
            # the left side of the array is sorted
            if nums[mid]>nums[right]:
                # find the number between the middle and left side
                if nums[left] <= target and target < nums[mid]:
                    right = mid -1
                else: 
                    left = mid + 1
            # the right side of the array is sorted
            else:
                # find the number between the middle and right side
                if nums[mid] < target and target <= nums[right]:
                    left = mid +1
                else:
                    right = mid -1
        return -1

def main():
    nums   = [4,5,6,7,0,1,2]
    target = 1
    solution = Solution()
    res = solution.search(nums, target)
    print(res)

main()


