# traverse the list twice
# def solve(nums):
#     first_max = second_max = float('-inf')
#     # get the first max value
#     for i in range(len(nums)):
#         first_max = max(first_max, nums[i])
#     # get the second max value 
#     for i in range(len(nums)):
#         if nums[i]!=first_max:
#             second_max = max(second_max, nums[i])
#     return second_max

# traverse the list once
def solve(nums):
    firstMax = secondMax = float('-inf')
    for i in range(len(nums)):
        if nums[i] > firstMax:
            firstMax = nums[i]
        if nums[i]!=firstMax and nums[i]>secondMax:
            secondMax = nums[i]
    return secondMax

def main():
    nums = [9, 2, 3, 6]
    print(solve(nums))

main()