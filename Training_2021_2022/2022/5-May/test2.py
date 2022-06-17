
def neetcode_solution(s, p):
    # Counters are not used because that's kinda cheating
    pCount, sCount = {}, {}
    for i in range(len(p)):
        # in case the key doesn't exist in the dictionary then use .get
        # if the key exists to get the value that is pointing
        # if there's no key then use the value 0
        pCount[p[i]] = 1 + pCount.get(p[i], 0)
        sCount[s[i]] = 1 + sCount.get(s[i], 0)

    res = [0] if sCount == pCount else []
    left = 0
    for r in range(len(p), len(s)):
        sCount[s[r]] = 1 + sCount.get(s[r], 0)
        sCount[s[left]] -= 1

        if sCount[s[left]] == 0:
            sCount.pop(s[left])

        left += 1
        if sCount == pCount:
            res.append(left)

    return res


def main():
    s = 'cbaebabacd'
    p = 'abc'
    res = neetcode_solution(s, p)
    print(res)


main()