'''
Given an integer array arr, count how many elements x there are,
such that x + 1 is also in arr.

If there're duplicates in arr, count them separately.

'''

def solve(m):

    # simple an efficient O(N) in time and space.
    hash_set = set(m)
    count = 0
    for x in m:
        if x+1 in hash_set:
            count+=1
    return count

    # horrible code and doesn't pass the l4 and l5 test cases

    # m.sort()
    # max_streak = 0
    # i = 0
    #
    # while i<len(m)-1:
    #     flag = m[i]+1
    #     count = 0
    #     gc =0
    #     for j in range(i+1,len(m)):
    #         if flag == m[j]:
    #             count +=1
    #             flag  +=1
    #     gc = gc + count
    #     max_streak = max(max_streak, gc)
    #     i+=1
    # return max_streak

def main():
    l = [5,3,3,0,1,2,2] #3
    l1 = [1,2,3] # 2
    l2 = [1,1,3,3,5,5,7,7] # 0
    l3 = [1,3,2,3,5,0] # 3
    l4 = [1,1,2,2] #2
    l5 = [1,1,2] #2
    print(solve(l5))

main()
