def solve(target, nums):
    total = window_start = 0
    # out of index
    result = len(nums) + 1
    for window_end in range(len(nums)):
        total += nums[window_end]
        while total >= target:
            result = min(result, window_end - window_start + 1)
            total -= nums[window_start]
            window_start += 1
    return result if result <= len(nums) else 0

def main():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    res = solve(target, nums)
    print(res)


main()