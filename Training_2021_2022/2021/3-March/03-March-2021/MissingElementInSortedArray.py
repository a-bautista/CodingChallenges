'''
    Given an integer array nums which is sorted in ascending order and all of its elements are unique
    and given also an integer k, return the kth missing number starting from the leftmost number of the array.

    Input: nums = [4,7,9,10], k = 1
    Output: 5
    Explanation: The first missing number is 5.

    The formula for this is: last (element - first element + 1) - len(array)
'''

def solve(nums, kElement):

    # Indicate to the computer how many missing numbers are left
    missingElementsInArray = (nums[-1] - nums[0] + 1) - len(nums)

    # if k> missing element then we can apply the formula return nums[-1]+k-missing
    if kElement > missingElementsInArray:
        return nums[-1] + kElement - missingElementsInArray

    # apply binary search
    last, left, right = 0, 0, len(nums)-1
    while left<=right:
        # set the middle indexed number from the array
        mid = left + (right - left)//2
        # determine the missing element with last element - initial element + 1 - len(nums) which is calculated
        # with the subtraction of ranges
        missingElementsInArray = (nums[mid] - nums[last] + 1) - (mid - last +1)

        if kElement > missingElementsInArray:
            # set the last variable as a reminder of where we were standing
            last = mid
            # subtract the missing element to our target element, so we can be closer
            kElement-=missingElementsInArray
            # move the left pointer to calculate a new range
            left = mid + 1
        else:
            # move the right pointer to calculate a new range
            right = mid - 1
    # nums[last] + kElement - missingElement but this latter is not needed becuase we have already defined it
    return nums[last] + kElement

def main():
    nums = [4,7,9,10]
    k = 4
    res = solve(nums, k)
    print(res)

main()

