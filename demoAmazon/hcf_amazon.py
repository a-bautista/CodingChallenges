''''
    The greatest common divisor (GCD), also called the highest common factor (HCF) of N numbers is the largest positive
    integer that divides all numbers without giving a remainder. Write an algorithm to determine the GCD of N positive integers (N),
    arr, a list of positive integers.

    Example:
        Input
            num =5
            arr = [2,4,6,8,10]
        Output
            2
'''

def generalizedGCD(num, arr):
    ret = arr[0]
    for i in range(num):
        ret = GCD(arr[i], ret)
        if ret == 1:
            return 1
        return ret

def GCD(x, y):
    if x == 0:
        return y
    return GCD(y % x, x)


print(generalizedGCD(5,[2,4,6,8,10]))