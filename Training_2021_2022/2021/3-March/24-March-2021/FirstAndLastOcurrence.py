class Solution:
    
    def solve(self, nums, target):
        
        firstPosition = self.binary_search(nums, True, target)
        if nums[firstPosition] != target:
            return [-1, -1]
        secondPosition = self.binary_search(nums, False, target)
        return [firstPosition, secondPosition-1]

    def binary_search(self, nums, flag, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) //2
            if nums[mid] > target or (flag and nums[mid] == target):
                right = mid
            else:
                left = mid + 1
        return left
        
        

def main():
    nums = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    solution = Solution()
    res = solution.solve(nums, 6)
    print(res)
    

main()