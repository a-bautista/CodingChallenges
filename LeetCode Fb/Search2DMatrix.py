

def search2DMatrix(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])

    # binary search
    left, right = 0, m * n - 1
    while left <= right:
        pivot_idx = (left + right) // 2
        # virtually, convert the matrix into a vector
        # pivot_idx // n gets the y location and pivot_idx gets the x location
        # the pivot element contains the real middle number
        pivot_element = matrix[pivot_idx // n][pivot_idx % n]

        if target == pivot_element:
            return True
        else:
            # the pivot is greater than the target, then move the right pointer
            if target < pivot_element:
                right = pivot_idx - 1
            # the pivot is less than the target, then move the left pointer
            else:
                left = pivot_idx + 1
    return False

'''
    Time complexity: O(log(mn))
    Space complexity: O(1)
'''