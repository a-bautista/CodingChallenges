def solve(nums):
    res = []
    pair_set = set()
    for pair in nums:
        pair_tup = tuple(pair)
        
        pair.reverse()
        reversed_pair = tuple(pair)
        if reversed_pair in pair_set:
            # elements are the same but in reversed order
            res.append(pair_tup)
            res.append(reversed_pair)
        else:
            pair_set.add(pair_tup)
    return res

def main():
    arr = [[1, 2], [4, 6], [4, 3], [6, 4], [5, 9], [3, 4], [9, 5]]
    symmetric = solve(arr)
    print(symmetric)

main()
