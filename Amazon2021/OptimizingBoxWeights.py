from collections import Counter
def optimizeBox(nums):
    numsDict = Counter(nums)
    numsArray = [(i, val) for i, val in numsDict.items()]
    numsArray.sort(key=lambda x: (-x[0], -x[0] * x[1]))

    A = []
    total = sum(nums)
    currSum = 0
    for i, j in numsArray:
        if currSum + (i * j) < total - currSum:
            currSum += i * j
            A += ([i] * j)
    if currSum >= total - currSum:
        return A
    else:
        return [x for x in nums if x not in A]


def main():
    print(optimizeBox([20, 15, 20, 50, 20]))

main()