from functools import reduce
def fibo(n):

    # check that the input is a positive integer
    if type(n)!=int:
        raise TypeError("n must be an integer number")

    if n < 1:
        raise ValueError("n must be a positive integer number")

    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def fibo2(n):
    if n <0:
        raise ValueError("N must be a positive integer")
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo2(n-1)+fibo2(n-2)

def main():
    fib_series =  lambda n:reduce(lambda x, _:x+[x[-1]+x[-2]], range(n-2),[0,1])
    print(fib_series(5))
    n = 5
    print(fibo(n))
    print(fibo2(n))


main()