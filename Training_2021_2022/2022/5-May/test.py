def solve(nums):
    res = []
    for i, i_val in enumerate(nums):
        temp_mult = 1
        for j, j_val in enumerate(nums):
            if i != j:
                temp_mult *= j_val
        res.append(temp_mult)
    return res


def optimal_solution(nums):
    res = [1 for _ in range(len(nums))]

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


def main():
    nums = [1, 2, 3, 4]
    res = optimal_solution(nums)
    print(res)


main()