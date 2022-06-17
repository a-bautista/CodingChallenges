def solve(nums):
    write = read = len(nums)-1
    while read >=0:
        if nums[read]!=0:
            nums[read], nums[write] = nums[write], nums[read]
            write-=1
        read-=1


def main():
    nums = [1, 10, 20, 0, 59, 63, 0, 88, 0]
    solve(nums)
    print(nums)

main()