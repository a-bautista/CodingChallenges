def aux_lists(nums):
    negative_values = []
    positive_values = []
    for i in range(len(nums)):
        if nums[i]<0:
            negative_values.append(nums[i])
        else:
            positive_values.append(nums[i])
    if len(negative_values)==0:
        return positive_values
    elif len(positive_values)==0:
        return negative_values
    else:
        negative_values.extend(positive_values)
        return negative_values

def rearrange(lst):
    leftMostPosEle = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if (lst[curr] < 0):
            # if not the last negative number
            if (curr is not leftMostPosEle):
                # swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # update the last position
            leftMostPosEle += 1
    return lst

def solve_no_extra_list(nums):
    index_left_element = 0
    for i in range(len(nums)):
        if nums[i]<0:
            if i is not index_left_element:
                nums[i], nums[index_left_element] = nums[index_left_element], nums[i]
                index_left_element +=1
    return nums

def main():
    print(aux_lists([10, -1, 20, 4, 5, -9, -6]))
    print(solve_no_extra_list([10, -1, 20, 4, 5, -9, -6]))

main()