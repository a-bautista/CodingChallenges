'''
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Example 1:

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

'''

from heapq import *
class SolutionHeap:

    def find_Kth_smallest_number(self, nums, k):
        maxHeap = []
        # put first k numbers in the max heap
        for i in range(k):
            heappush(maxHeap, -nums[i])

        # go through the remaining numbers of the array, if the number from the array is smaller than the
        # top(biggest) number of the heap, remove the top number from heap and add the number from array
        for i in range(k, len(nums)):
            if -nums[i] > maxHeap[0]:
                heappop(maxHeap)
                heappush(maxHeap, -nums[i])

        # the root of the heap has the Kth smallest number
        return -maxHeap[0]

'''
    Time complexity: O(N*Log(K))
    Space complexity: O(K) store k smallest numbers in the heap
    
'''

class SolutionQuickSelect:
    def find_Kth_smallest_number(self, nums, k):
      return self.find_Kth_smallest_number_rec(nums, k, 0, len(nums) - 1)


    def find_Kth_smallest_number_rec(self, nums, k, start, end):
      p = self.partition(nums, start, end)

      if p == k - 1:
        return nums[p]

      if p > k - 1:  # search lower part
        return self.find_Kth_smallest_number_rec(nums, k, start, p - 1)

      # search higher part
      return self.find_Kth_smallest_number_rec(nums, k, p + 1, end)


    def partition(self, nums, low, high):
      if low == high:
        return low

      pivot = nums[high]
      for i in range(low, high):
        # all elements less than 'pivot' will be before the index 'low'
        if nums[i] < pivot:
          nums[low], nums[i] = nums[i], nums[low]
          low += 1

      # put the pivot in its correct place
      nums[low], nums[high] = nums[high], nums[low]
      return low


def main():

  solution = SolutionHeap()
  print("Kth smallest number is: " +
        str(solution.find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(solution.find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(solution.find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()