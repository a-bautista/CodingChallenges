"""
    Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should
    also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]

    Input: arr = [1,2,3,4,5], k = 4, x = -1
    Output: [1,2,3,4]


"""
class Solution:
    def findClosestElements(self, A, k, x):
        left, right = 0, len(A) - k
        while left < right:
            mid = int((left + right) / 2)
            # determine if you are closer to the left or to the right
            # x - A[mid] closer to the left
            # A[mid + k] - x closer to the right
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k]

def main():
    arr = [1,2,3,4,5,6,7]
    # k elements
    # x is our target
    solution = Solution()
    res = solution.findClosestElements(arr, 2, 6)
    print(res)

main()

