

def solution_triplets_sum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        # edge case: repeated values such as [-1,1,0,-1,1,0,-1,1,0]
        if i>0 and nums[i]==nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            current_sum = nums[left] + nums[right] + nums[i]
            if current_sum < 0:
                left +=1
            elif current_sum > 0:
                right -=1
            else:
                res.append((nums[left], nums[right], nums[i]))
                # edge case avoid counting the values you have already considered into the array, i.e., [-1,1,0,-1,1,0,-1,1,0]
                while left <= right and nums[left]==nums[left+1]:
                     left+=1
                while left<=right and nums[right]==nums[right-1]:
                     right-=1
                left+=1
                right-=1
    return res

def main():
    nums = [-5, 2, -1, -2, 3]
    nums1 = [-1,1,0,-1,1,0,-1,1,0]
    res = solution_triplets_sum(nums1)
    print(res)

main()