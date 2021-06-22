'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets
such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

In the array, we need to verify if we can arrive to the target value
 which is sum(array)/2.

 We need to create an array that moves from right to left and verify if we
 have a complement that added with the current ith number in our original array
 adds up to the target number.

 [1,2,4,5]
sum = 12
target = 6

current_i = 1

 Can I reach to 6 with 1? No because I don't have its complement.
 [0,1,2,3,4,5,6]
  T F F F F F F
            C _

Can I reach to 5 with 1? No because I don't have its complement.
[0,1,2,3,4,5,6]
T F F F F F F
          C _
....

Can I reach to 1 with 1? Yes because I have its complement 0.
[0,1,2,3,4,5,6]
 T T F F F F F
 C _

[1,2,4,5]
current ith = 2

Can I reach to 6 with 2? No because I don't have its complement.
[0,1,2,3,4,5,6]
 T T F F F F F
         c   _

Can I reach to 5 with 2? No because I don't have its complement.
[0,1,2,3,4,5,6]
 T T F F F F F
       c   _
Can I reach to 3 with 2? Yes! I have its complement which is 1.
[0,1,2,3,4,5,6]
 T T F F F F F
   c   _
Can I reach 2 with 2? Yes! I have its complement which is 0.
[0,1,2,3,4,5,6]
 T T F T F F F
 c   _

[1,2,4,5]
Current_i = 4

Can I reach 6 with 4? Yes!!! I have its complement which is 2.
[0,1,2,3,4,5,6]
 T T T T F F F
     c       _

The result is True.
'''


class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        # determine if it is possible to come up with a partition
        if total % 2 == 1: return False

        target = total / 2  # target sum
        s = set([0])  # stores the sums of the subsets with the base case 0

        for n in nums:
            sums_with_n = []  # stores the sums of the subsets that contain n
            # Verify if we've arrived to the target based on the complement
            for i in s:
                if i + n == target: return True
                if i + n < target:
                    sums_with_n.append(i + n)
            s.update(sums_with_n)
        return False

def main():
    s = [1,2,4,5]
    solution = Solution()
    res = solution.canPartition(s)
    print(res)

main()

'''
    Each number in the array can be picked or not picked to form the subset of array to have a target 
    sum. Here we can scan through the array, and store the sums of the subsets that include or not 
    include the current number. We can use a set to store the sums to avoid duplicates.
'''