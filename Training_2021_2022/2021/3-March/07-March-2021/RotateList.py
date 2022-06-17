def right_rotate(lst, k):
    k = k % len(lst)
    rotatedList = []
    # start from the k element until the end
    for item in range(len(lst) - k, len(lst)):
        rotatedList.append(lst[item])
    # start from the beginning of the list until the kth element
    for item in range(0, len(lst) - k):
        rotatedList.append(lst[item])
    return rotatedList



def main():
    print(right_rotate([10, 20, 30, 40, 50], abs(3)))

main()