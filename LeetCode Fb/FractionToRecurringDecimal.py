def fractionToDecimal(numerator, denominator):
    num, den = numerator, denominator
    # edge cases
    if not den:  # denominator is 0
        return
    if not num:  # numerator is 0
        return "0"

    res = []
    # add the sign to the result
    if (num < 0) ^ (den < 0):
        res.append("-")

    # remove the negative values from the num and den in case we find them
    if num <0:
        num = (-1)*(num)
    if den <0:
        den = (-1)*(den)

    #store the quotient part in the rersult and then compute the remainder
    res.append(str(num//den))
    remain = num % den

    # if there's not any remainder then it means we have only integral part and we are done
    if not remain:
        return "".join(res)

    # add the factional part
    res.append(".")
    # create a dictionary to keep the remainder part in case the number start being recursive in the fraction part
    dic = {}
    while remain:
        # the remainder starts being recursive then add the parenthesis to indicate it
        if remain in dic:
            res.insert(dic[remain], "(")
            res.append(")")
            break

        # add the remainder to the dictionary to make sure later if the decimal part will be recursive
        dic[remain] = len(res)

        # multiply the remainder by 10 then get the integral part, so you can get the quotient
        quotient = ((remain*10) // den)
        remain =  (remain*10) % den

        # append the quotient to the result
        res.append(str(quotient))
    return "".join(res)


def main():
    numerator = -12434308
    denominator = -123
    num1 = -50
    den2 = 8
    res = fractionToDecimal(num1, den2)
    print(res)

main()

'''
    Time complexity: O(N) because of the remainder
    Space complexity: O(1)
    
    Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

    If the fractional part is repeating, enclose the repeating part in parentheses.

    If multiple answers are possible, just return any of them.
'''