def fact_iter(num):
    if num < 0:
        return ValueError("The number must be positive")

    if num == 0 or num == 1:
        return 1

    fact = 1
    while(num>0):
        fact *=num
        num-=1
    return fact

def main():
    res = fact_iter(6)
    print(res)

main()