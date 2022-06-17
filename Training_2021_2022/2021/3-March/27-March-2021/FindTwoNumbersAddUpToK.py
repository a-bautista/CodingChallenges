'''
    Given an array and a target, find two numbers that add up to a target.

    Input: 
        nums = [1,2,3,4]
        target = 5
        output: [2,3]
    Input:
        nums = [1, 21, 3, 14, 5, 60, 7, 6]
        target = 81

'''
def solve(nums, k):
    setTable = set()
    for i in range(len(nums)):
        if k - nums[i] in setTable:
            return [k - nums[i], nums[i]]
        setTable.add(nums[i])

def main():
    nums = [1,2,3,4]
    target = 5
    # nums = [1, 21, 3, 14, 5, 60, 7, 6]
    # target = 81
    res = solve(nums, target)
    print(res)

main()

