# Solution 1: Create a new list
def merge_two_sorted_lists_method_1(list1, list2):
    res = []
    index_l1  = 0
    index_l2  = 0
    index_result = 0

    # we need to define our final list based on the lengths of list1 and list2
    # if not then we will have index out of range in the results list
    for i in range(len(list1)+len(list2)):
        res.append(i)

    # traverse both lists and compare the element of each list to indicate which element goes first
    while(index_l1<len(list1) and index_l2<len(list2)):
        # if the element in list1 is less than list2 then add it to the result
        if list1[index_l1] <= list2[index_l2]:
            res[index_result]=list1[index_l1]
            index_l1+=1
            index_result+=1
        else:
            res[index_l2] = list2[index_l2]
            index_l2+=1
            index_result+=1

    # if there are existing elements in list1 (based on the index_l1) then continue adding
    # the rest of elements from that list
    while (index_l1<len(list1)):
        res[index_result]=list1[index_l1]
        index_l1+=1
        index_result+=1

    # if there are existing elements in list2 (based on the index_l2) then continue adding
    # the rest of elements from that list
    while (index_l2<len(list2)):
        res[index_result]=list2[index_l2]
        index_l2+=1
        index_result+=1
    return res

# Solution 2: In place

def merge_two_sorted_lists_method_2(l1, l2):

    index_l1  = 0
    index_l2  = 0
    while (index_l1 < len(l1) and index_l2 < len(l2)):

        if l1[index_l1]>l2[index_l2]:
            # the element of list2 will be inserted before any current element of list1
            # insert the current element of the second list in place of the current element of the first list
            # and increment both index variables by 1
            l1.insert(index_l1, l2[index_l2])
            # move onto the next element of list1
            index_l1+=1
            # move onto the next element of list2
            index_l2+=1
        # only move the first element in list1 because that means the element in list2 is greater than list1
        else:
            index_l1+=1

    # append the leftovers from list2 to list1
    if (index_l2 < len(l2)):
        l1.extend(l2[index_l2:])
    return l1


def main():
    l1 = [1,2,4]
    l2 = [1,3,5,6,7]
    res = merge_two_sorted_lists_method_2(l1, l2)
    print(res)

main()