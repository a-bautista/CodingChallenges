def solve(nums, rotation):

    res = []
    initial = (rotation%len(nums))+1
    for i in range(initial, len(nums)):
        res.append(nums[i])

    for i in range(0, initial):
        res.append(nums[i])
        
    print(res)

def main():
    nums = [2,3,4,5,6]
    rotation = 2
    solve(nums, rotation)

main()

'''
    input:
    nums = [2,3,4,5,6]
    rotation = 2

    output:
    nums = [5,6,2,3,4]

    get the k value of rotation in the array, that is, I want to get the values 5 and 6

'''