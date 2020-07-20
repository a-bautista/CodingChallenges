def fractionToDecimal(numerator, denominator):
    num, den = numerator, denominator
    if not den:  # denominator is 0
        return
    if not num:  # numerator is 0
        return "0"
    res = []
    if (num < 0) ^ (den < 0):
        res.append("-")  # add the sign
        # remove the negative values
    if num <0:
        num = (-1)*(num)
    if den <0:
        den = (-1)*(den)

    #num, den = abs(num), abs(den)
    res.append(str(num//den))
    remain = num % den
    # if there's not any remainder then it means we have only integral part
    if not remain:
        return "".join(res)
    # add the factional part
    res.append(".")
    # create a dictionary to keep the remainder part
    dic = {}
    while remain:
        # the remainder recurs, so let's add the parenthesis
        if remain in dic:
            res.insert(dic[remain], "(")
            res.append(")")
            break
        dic[remain] = len(res)
        # multiply the remainder by 10, so you can get the quotient
        quotient = ((remain*10) // den)
        remain =  (remain*10) % den
        #div, remain = divmod(remain*10, den)
        res.append(str(quotient))
    return "".join(res)


def main():
    numerator = 12434308
    denominator = 123
    res = fractionToDecimal(numerator, denominator)
    print(res)

main()

'''
    Time complexity: O(N) because of the remainder
    Space complexity: O(1)
'''