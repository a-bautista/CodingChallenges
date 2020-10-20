'''
    Given an unsorted array of integers and an element x, find if x is present in array using Front and Back search.

    Examples :

    Input : arr[] = {10, 20, 80, 30, 60, 50,
                         110, 100, 130, 170}
              x = 110;
    Output : Yes

    Input : arr[] = {10, 20, 80, 30, 60, 50,
                         110, 100, 130, 170}
               x = 175;
    Output : No

'''

def solve(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        if nums[left]==target:
            return left
        if nums[right]==target:
            return right
        left +=1
        right-=1
    return -1


def main():
    nums = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    target = 60
    print(solve(nums, target))

main()