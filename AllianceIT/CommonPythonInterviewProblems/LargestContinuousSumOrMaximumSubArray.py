'''
    Given an array of integers (positive and negative) find the largest
    continuous sum.
    input: [1,2,-1,3,4,10,10,-10,-1]
    output: 29

'''
def solve(arr):

    if len (arr)==0:
        return 0

    curr_sum = max_sum = arr[0]
    for num in arr[1:]:

        # the line from below is used to start the initial point where the max sum occurs
        curr_sum = max(num, curr_sum+num)
        max_sum = max(max_sum, curr_sum)
    return max_sum


def main():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    res = solve(arr)
    print(res)

main()
