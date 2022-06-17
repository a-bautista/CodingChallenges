'''
    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

'''

def search2DMatrix(matrix, target):
    '''
        1. Get the length of m rows and n columns
        2. Do a binary search because the grid is sorted
        3. Get the middle number: middle_num = left + (right - left) // 2
        4. Get the real middle number in the matrix by doing matrix[middle_num // n][middle_num % n]
        5. Apply binary search based on the middle number
    '''
    m = len(matrix)
    n = len(matrix[0])
    if m == 0 or n == 0:
        return False

    start = 0
    end = m*n-1
    while start <= end:
        # the pivot is the index that we use for the middle number
        pivot = start + (end - start) // 2
        # convert the matrix into a vector to get the real middle number
        middleNum = matrix[pivot // n][pivot % n]

        # Case I. Number was found
        if middleNum == target:
            return True
            
        else:
            # Case II. The middle number is less than the target, discard the left side   
            if middleNum <= target:
                start = pivot + 1
            
            # Case III. The middle number is greater than the target, discard the right side
            else:
                end = pivot - 1
    
    return False
        
        
def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    res = search2DMatrix(matrix, target)
    print(res)

main()

'''
    Time complexity: O(log(mn))
    Space complexity: O(1)
'''