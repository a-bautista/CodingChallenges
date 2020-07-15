class Solution:
    def search(self, nums: List[int], target: int) -> bool:    
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            # target is in the second half
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # target is in the first half half        
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return nums[l] == target
        
def main():

    nums = [2,5,6,0,0,1,2]
    solution = Solution()
    res = solution.search(nums, 6)
    print(res)

main()

'''
    Time complexity: O(Log(N))
    Space complexity: O(1)
'''
