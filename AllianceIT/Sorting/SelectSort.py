from random import randrange

def select_sort(nums):
    for number in range(len(nums)-1, 0, -1):

        max_position = 0
        for other_number in range(1,number+1):
            if nums[other_number] > nums[max_position]:
                max_position = other_number

        nums[number], nums[max_position] = nums[max_position], nums[number]
    return nums

def main():
    nums = [randrange(0,1000) for _ in range(10)]
    res = select_sort(nums)
    print(res)

main()