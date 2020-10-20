'''
    Given a string in the form 'AAABBCCCCDD' compress it to become A3B2C4D2.
    AAAaaa = A3a3
'''

def solve(s):
    if len(s) == 1:
        return s + str(1)

    i = 1
    res = ""

    count = 1
    while i <= len(s) - 1:

        if s[i] == s[i - 1]:
            count += 1
        else:
            res = res + s[i - 1] + str(count)
            count = 1
        i += 1
    res = res + s[i - 1] + str(count)
    return res


def main():
    st = "AAABB"
    res = solve(st)
    print(res)

main()
