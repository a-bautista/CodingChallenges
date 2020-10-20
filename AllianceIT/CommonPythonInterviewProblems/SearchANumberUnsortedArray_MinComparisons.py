def search(arr, x):

    n = len(arr)
    # 1st comparison
    if (arr[n - 1] == x):
        return "Found"

    backup = arr[n - 1]
    arr[n - 1] = x

    # no termination condition and
    # thus no comparison
    i = 0
    while (i < n):

        # this would be executed at-most n times
        # and therefore at-most n comparisons
        if (arr[i] == x):

            # replace arr[n-1] with its actual
            # element as in original 'arr[]'
            arr[n - 1] = backup

            # if 'x' is found before the '(n-1)th'
            # index, then it is present in the
            # array final comparison
            if (i < n - 1):
                return "Found"

            # else not present in the array
            return "Not Found"
        i = i + 1

def main():
    nums = [4, 6, 1, 5, 8]
    target = 5
    print(search(nums, target))

main()