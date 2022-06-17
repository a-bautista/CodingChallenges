
'''
    Time complexity: O(N)**2
'''
def findSum(nums, k):
    # Write your code here
    myDict = dict()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            suma = nums[i]+nums[j]
            if suma == k:
                return [nums[i], nums[j]]
            elif suma in myDict:
                return myDict.get(suma)
            elif suma not in myDict:
                myDict[suma] = [nums[i], nums[j]]
    return myDict


'''
    Time complexity: O(N)
'''
def findSumSet(nums, k):
    # k = value1 + value2
    # k - value1 = value2 and value2 is stored in the hash table
    foundValues = set()
    for element in nums:
        if  k - element in foundValues:
            return [k - element, element]
        foundValues.add(element)
    return foundValues

print(findSumSet([1, 21, 3, 14, 5, 60, 7, 6],81))