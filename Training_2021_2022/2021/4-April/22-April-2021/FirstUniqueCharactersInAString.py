from collections import OrderedDict
def solve(s):
    ordDict = OrderedDict()
    stack = []
    for letter in s:
        if letter not in ordDict:
            ordDict[letter] = 0
        else:
            ordDict[letter]+=1

    minVal = float('inf')
    for letter, count in ordDict.items():
        minVal = min(minVal, count)

    if minVal==0:
        # find the key value based on the value
        keys = list(ordDict.keys())
        values = list(ordDict.values())
        index  = keys[values.index(minVal)]
        return s.index(index)
    else:
        return -1

def real_solution(s):
    count = collections.Counter(s)
    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx     
    return -1


def main():
    s = "aabb"
    res = solve(s)
    print(res)

main()