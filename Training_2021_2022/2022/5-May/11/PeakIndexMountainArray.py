'''
    Let's call an array arr a mountain if the following properties hold:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... arr[i-1] < arr[i]
    arr[i] > arr[i+1] > ... > arr[arr.length - 1]
    Given an integer array arr that is guaranteed to be a mountain, return any i such that
        arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

    Example 1:
        Input: arr = [0,1,0]
        Output: 1

    Example 2:
        Input: arr = [0,2,1,0]
        Output: 1

    Example 3:
        Input: arr = [0,10,5,2]
        Output: 1

    Solution 1:
    Linear Scan

    def sol(nums):
        my_dict = {}
        max_val = float('-inf')
        max_index = 0

        for index, value in enumerate(nums):
            my_dict[index] = value

        for i, v in my_dict.items():
            if v > max_val:
                max_val = v
                max_index = i

        return max_index

    Time complexity: O(N)
    Space complexity: O(1)

    Solution 2: Binary search

    left, right = 0, len(nums)-1
    while left < right:
        middle = left + (right- left)//2
        if nums[middle]<nums[middle+1]:
            left = middle + 1
        else:
            right = middle
    return left

    Time complexity: O(Log.N)
    Space complexity: O(1)

'''


def sol(nums):
    left, right = 0, len(nums)-1
    while left < right:
        middle = left + (right- left)//2
        if nums[middle]<nums[middle+1]:
            left = middle + 1
        else:
            right = middle
    return left

def main():

    nums = [0,1,0]
    nums2 = [0,2,1,0]
    res = sol(nums)
    print(res)

main()