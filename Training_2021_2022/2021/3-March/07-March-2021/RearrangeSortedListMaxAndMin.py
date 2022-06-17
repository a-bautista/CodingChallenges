def solve(nums):
    res = []
    for i in range(len(nums)//2):
        res.append(nums[-1-i])
        res.append(nums[i])
    if len(nums)//2 == 1:
        res.append(nums[i])
    return res   


# O(1) space
def max_min(lst):
    # Return empty list for empty list
    if (len(lst) is 0):
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst

def main():
    print(solve([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

main()