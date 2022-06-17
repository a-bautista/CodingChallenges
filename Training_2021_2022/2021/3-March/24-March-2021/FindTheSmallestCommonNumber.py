'''
    In the example below,​ you are given three positive integer arrays which are sorted in ascending order.
    You have to find the smallest number that is common in all three arrays. Return -1 if the smallest 
    common number is not found.
'''

def solve(nums1, nums2, nums3):
    i = 0
    j = 0
    k = 0

    while i < len(nums1) and j < len(nums2) and k < len(nums3):

        # a < b < c
        # a < b then a < c
        if nums1[i] == nums2[j] and nums2[j]==nums3[k]:
            return nums1[i]

        # Condition 1: nums1[i] is less than nums2[j] and nums3[k]
        if nums1[i] <= nums2[j] and nums1[i] <= nums3[k]:
            i+=1
        
        # Condition 2: nums2[j] less than nums1[i] and nums2[j] less than nums3[k]
        elif nums2[j] <= nums1[i] and nums2[j] <= nums3[k]:
            j+=1

        # Condition 3: nums3[k] is less than nums1[i] and nums3 is less than nums2[j]
        else:
            k+=1

def main():
    v1 = [8, 7, 10, 25, 30, 63, 64]
    v2 = [1, 4, 5, 6, 7, 8, 50]
    v3 = [1, 6, 8, 14]
    print(solve(v3, v2, v1))

main()