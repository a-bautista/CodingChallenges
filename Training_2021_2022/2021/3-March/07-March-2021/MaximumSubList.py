# Kadane's algorithm (DP)
def solve(nums):

    currentMax = nums[0]
    maxGlobal = nums[0]

    for i in range(1, len(nums)):

        if currentMax<0:
            currentMax = nums[i]
        else:
            currentMax+=nums[i]
            if maxGlobal < currentMax:
                maxGlobal = currentMax
    return maxGlobal

def main():
    lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
    print("Sum of largest subarray: ", solve(lst))

main()