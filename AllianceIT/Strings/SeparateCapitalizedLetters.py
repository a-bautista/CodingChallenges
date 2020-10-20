def solve(s):
    caps = set()
    sbuilder = []
    for i in range(len(s)):
        if s[i] == s[i].upper():
            caps.add(i)

    i = 0
    while i <= len(s) - 1:
        if i in caps:
            # beginning case
            if i == 0 and i <= len(s) - 1:
                sbuilder.append(s[i])
                #sbuilder.append(" ")

            # middle case
            # elif i == len(s) - 1:
            #     sbuilder.append(" ")
            #     sbuilder.append(s[i])

            # ending case
            else:
                sbuilder.append(" ")
                sbuilder.append(s[i])
                #sbuilder.append(" ")
        else:
            sbuilder.append(s[i])
        i += 1
    return "".join(sbuilder)


def main():
    s1 = "TheLinearAlgebra" # passed
    s2 = "atThisMOment"     # passed
    s3 = "atThisMoment"     # passed
    s4 = "iT"               # passed
    s5 = "itT"              # passed
    s6 = "iTT"              # passed
    s7 = "iTiT"
    res = solve(s4)
    print(res)


main()