from functools import lru_cache

@lru_cache(maxsize=1000)
def fibo(n):

    if n == 1:
        return 0
    elif n ==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def main():
    print(fibo(10))

main()