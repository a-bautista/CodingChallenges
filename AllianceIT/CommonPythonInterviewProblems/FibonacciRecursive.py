from functools import reduce
def fibo_starting_at_one(n):

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
        return fibo_starting_at_one(n-1)+fibo_starting_at_one(n-2)

def fibo_starting_at_zero(n):
    if n <0:
        raise ValueError("N must be a positive integer")
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo_starting_at_zero(n-1)+fibo_starting_at_zero(n-2)

def main():
    fib_series =  lambda n:reduce(lambda x, _:x+[x[-1]+x[-2]], range(n-2),[0,1])
    print(fib_series(5))
    n = 5
    print(fibo_starting_at_one(n))
    print(fibo_starting_at_zero(n))


main()