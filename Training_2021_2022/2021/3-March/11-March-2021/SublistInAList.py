def is_subset(nums, sublist):
    s = set(nums)
    for value in sublist:
        if value not in s:
            return False
    return True

def main():
    nums = [1,2,3,4,5,6]
    subList = [5,4]
    res = is_subset(nums, subList)        
    print(res)

main()
