from functools import cmp_to_key
def myComparator(a,b):

    sum_a=sum(a[1])
    sum_b=sum(b[1])

    if sum_a < sum_b:
        return -1
    elif sum_a > sum_b:
        return 1

def main():
    items = [(2, [3, 4, 5]), (3, [1, 0, 0, 0, 1]), (4, [-1]), (10, [1, 2, 3])]
    res = sorted(items, key=cmp_to_key(myComparator))
    print(res)

main()

'''
    Explanation:
        
        [3,4,5]     = [12] (a)
        [1,0,0,0,1] = [2]  (b)
        [-1]        = [-1] (c)
        [1,2,3]     = [6]  (d)
    
    [a,b,c,d]
    compare a and b as b<a then True, -1
    [b,a,c,d]
    compare b and c as c<b, then True, -1
    [c,b,a,d]
    compare c and d as d<c, then False, 1
    compare b and d as d<b, then False, 1
    compare a and d as d<a, then True, -1
    [c,b,d,a]
'''