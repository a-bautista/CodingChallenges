'''
    Given an unsorted array, find the missing number in the array.
    [1,2,3,4,5] and [5,1,3,4].
'''

from collections import defaultdict
def solve(complete_arr, incomplete_arr):

    # the int of the defaultdict is the key of the dict
    # if the key is not found then just add this new key
    dd = defaultdict(int)

    # create the dictionary with all the numbers from the
    # missing array
    for num in incomplete_arr:
        dd[num] +=1

    for num2 in complete_arr:
        # because num2 doesn't exist in this default dict then
        # the key will be 0 and this will be our missing number
        if dd[num2] == 0:
            return num2
        else:
            dd[num2] -=1
    return

def solXor(arr1, arr2):
    result = 0
    for num in arr1 + arr2:
        result^=num
        print(result)
    return result

def main():
    arr1 = [1,2,3,4,5]
    arr2 = [5,1,3,4]
    print(solXor(arr1, arr2))


main()

'''
    Time complexity: O(N)
    Space complexity: O(1)
'''