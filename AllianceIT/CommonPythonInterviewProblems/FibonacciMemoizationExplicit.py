memo = {}
def fiboDP(n):

    if type(n)!=int:
        raise TypeError("Value must be an integer")

    if n<1:
        raise ValueError("Value must be a positive integer")

    # check if the value is in the dictionary
    if n in memo:
        return memo[n]

    # if n == 0:
    #     value = ''

    if n == 1:
        value = 0

    elif n == 2:
        value = 1

    else:
        value = fiboDP(n-1)+fiboDP(n-2)

    memo[n] = value
    return value

def main():
    res = []
    n = 5
    for i in range(1,n+1):
        res.append(fiboDP(i))
        print(i,":",fiboDP(i))
    print(' '.join(map(str, res)))
    #print(" ".join(res))

main()