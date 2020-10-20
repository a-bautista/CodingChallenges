from collections import defaultdict

'''
    Easy solution 
    len(set(s))==len(s)
'''

def solve(s):
    if len(s) == 0:
        return True

    if len(s) == 1:
        return True

    d = defaultdict(str)

    for i in range(len(s)):
        if s[i] not in d.keys():
            d[s[i]] = 1
        else:
            d[s[i]] += 1

    for i, v in d.items():
        if v > 1:
            return False
    return True


def main():
    st = "ABCDDeg"
    res = solve(st)
    print(res)


main()
