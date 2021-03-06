'''
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

    Note:

    The solution set must not contain duplicate triplets.

    Example:

    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

    1. Start by sorting the array.
    2. You need to compare each value of the array with two pointers, so you start the loop from i=0 until
        range(len(nums))-2.
    3. Avoid repeated values with the following line:
        if i > 0 and nums[i] == nums[i-1]: continue
    4. Set the pointers left and right and initialize the while loop l<r.
    5. Sum the current value + left + right and if the result <0 then increase the left pointer, else if the result >0
    then increase the right pointer, else we found the values that add up to 0, so store them in a list called result.
    6. Increase the values of the 2 pointers and do 2 while loops for each pointer where l<r and nums[l] == nums[l+1]
    then increase the left pointer and while l<r and nums[r] == nums[r-1] then decrease the right pointer.
    These two conditions are necessary to avoid repeated values that you have already accounted.
'''

class Solution:
    def solve(self, nums):
        res = []
        nums.sort()
        # compare each value in the array
        for i in range(len(nums) - 2):
            # Avoid repeated values that you've already accounted for.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # set the pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    # add the 3 values that add up to 0
                    res.append((nums[i], nums[l], nums[r]))
                    # edge case avoid counting the values you have already considered into the array, i.e., [-1,1,0,-1,1,0,-1,1,0]
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # increase the pointers to break the loop
                    l += 1
                    r -= 1
        return res

def main():
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    res = solution.solve(nums)
    print(res)

main()

# def search_triplets(arr):
#   arr.sort()
#   triplets = []
#   for i in range(len(arr)):
#     if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
#       continue
#     search_pair(arr, -arr[i], i+1, triplets)
#   return triplets
#
#
# def search_pair(arr, target_sum, left, triplets):
#   right = len(arr) - 1
#   while(left < right):
#     current_sum = arr[left] + arr[right]
#     if current_sum == target_sum:  # found the triplet
#       triplets.append([-target_sum, arr[left], arr[right]])
#       left += 1
#       right -= 1
#       while left < right and arr[left] == arr[left - 1]:
#         left += 1  # skip same element to avoid duplicate triplets
#       while left < right and arr[right] == arr[right + 1]:
#         right -= 1  # skip same element to avoid duplicate triplets
#     elif target_sum > current_sum:
#       left += 1  # we need a pair with a bigger sum
#     else:
#       right -= 1  # we need a pair with a smaller sum


# def main():
#   print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
#   print(search_triplets([-5, 2, -1, -2, 3]))
#
# main()

'''
    Time complexity: O(N**2) and sorting takes O(N*Log(N)) = O((N**2)+(N*Log(N)))
    Space complexity: O(1) 
    
    [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    [[-5, 2, 3], [-2, -1, 3]]
'''