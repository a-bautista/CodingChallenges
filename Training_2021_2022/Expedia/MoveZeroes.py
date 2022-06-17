def solve(nums):
    readArray = len(nums)-1
    writeArray = len(nums)-1
    while readArray>=0:
        if nums[readArray]!=0:
            nums[writeArray]=nums[readArray]
            writeArray-=1
        readArray-=1

    while writeArray>=0:
        nums[writeArray]=0
        writeArray-=1
    return nums

def main():
    nums = [1, 10, -1, 11, 5, 0, -7, 0, 25, -35]
    res = solve(nums)
    print(res)

main()