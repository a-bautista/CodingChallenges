

def findPairs(a, b, target):
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    l, r = 0, len(b) - 1
    ans = []
    curDiff = float('inf')
    while l < len(a) and r >= 0:
        id1, i = a[l]
        id2, j = b[r]
        if (target - i - j == curDiff):
            ans.append([id1, id2])
        elif (i + j <= target and target - i - j < curDiff):
            ans.clear()
            ans.append([id1, id2])
            curDiff = target - i - j
        if (target > i + j):
            l += 1
        else:
            if target == i + j:
                tmp_l = l
                while a[tmp_l][1] + b[r][1] == target:
                    tmp_l += 1
                    if tmp_l == len(a):
                        break
                    if a[tmp_l][1] + b[r][1] == target:
                        ans.append([a[tmp_l][0], b[r][0]])
            r -= 1

    ans.sort(key=lambda x: x[1])
    ans.sort(key=lambda x: x[0])
    return ans


# test 1
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
expected = [[2, 1]]
assert findPairs(a, b, target) == expected

# test 2
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20
expected = [[3, 1]]
assert findPairs(a, b, target) == expected

# test 3
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20
expected = [[1, 3], [3, 2]]
assert findPairs(a, b, target) == expected

# test 4
a = [[1, 5], [2, 5]]
b = [[1, 5], [2, 5]]
target = 10
expected = [[1, 1], [1, 2], [2, 1], [2, 2]]
assert findPairs(a, b, target) == expected

'''
    Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the 
    second integer represents a value. Your task is to find an element from a and an element form b such that the sum 
    of their values is less or equal to target and as close to target as possible. Return a list of ids of selected elements. 
    If no pair is possible, return an empty list.
    
    Input:
    a = [[1, 2], [2, 4], [3, 6]]
    b = [[1, 2]]
    target = 7

    Output: [[2, 1]]

    Explanation:
    There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
    Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
'''