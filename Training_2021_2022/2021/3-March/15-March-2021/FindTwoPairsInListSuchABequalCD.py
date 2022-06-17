# def solve(nums):
#     result = []
#     my_dict = dict()
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             suma = nums[i] + nums[j]

#             if suma not in my_dict:
#                 my_dict[suma] = [nums[i], nums[j]]

#             else:
#                 prev_pair = my_dict.get(suma)
#                 second_pair = [nums[i], nums[j]]
#                 result.append(prev_pair)
#                 result.append(second_pair)
#                 return result
#     return result

def solve(nums):
	res = []
	myDict = dict()
	
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			
			suma = nums[i] + nums[j]
			
			if suma not in myDict:
				myDict[suma] = [nums[i], nums[j]]
			
			else:
				# get the other pair
				prev = myDict.get(suma)
				res.append(prev)
				res.append([nums[i], nums[j]])
				return res
		# return empty list in case there wasn't any value in the list
	return res

def main():
    nums  = [3, 4, 7, 2, 12, 9, 0]
    nums2 = [-1, 2, 4, 3]
    res = solve(nums)
    print(res)

main()

def main():
    nums  = [3, 4, 7, 2, 12, 9, 0]
    nums2 = [-1, 2, 4, 3]
    res = solve(nums)
    print(res)

main()