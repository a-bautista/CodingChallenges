def sol(nums, target):
    left = 0
    right = len(nums)-1
    while left<=right:
        middle = left + (right - left)//2
        if nums[middle]==target:
            return middle
        elif nums[middle] < target:
            left = middle +1 
        else:
            right = middle -1
    return left

def main():
    nums = [1,2,3]
    target = 3
    sol(nums, target)

main()