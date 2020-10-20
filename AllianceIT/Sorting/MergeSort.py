def merge_sort(nums):

    if len(nums) > 1:

        mid = len(nums)//2
        leftHalf = nums[:mid]
        rightHalf = nums[mid:]

        merge_sort(leftHalf)
        merge_sort(rightHalf)

        i = j = k =0
        # copy data to temp arrays L[] and R[]
        while i < len(leftHalf) and j < len(rightHalf):

            if leftHalf[i] < rightHalf[j]:
                nums[k] = leftHalf[i]
                i+=1

            else:
                nums[k] = rightHalf[j]
                j +=1
            k+=1

        while i < len(leftHalf):
            nums[k] = leftHalf[i]
            i +=1
            k +=1

        while j < len(rightHalf):
            nums[k] = rightHalf[j]
            j +=1
            k +=1

    return nums

def main():

    nums = [38,27,43,3,9,82,10]
    res = merge_sort(nums)
    print(res)

main()
