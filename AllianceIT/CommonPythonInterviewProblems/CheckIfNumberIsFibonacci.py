# formula:
# if n is True in either one of these cases then it is a Fibo number:
# (5*n**2 + 4) or (5*n**2 -4)

from math import sqrt
def perfect_square(number):
    res = int(sqrt(number))
    return res * res == number

def fibo_number(num):
    return perfect_square(5*num*num+4) or perfect_square(5*num*num-4)

def main():
    for i in range(0,1000):

        if (fibo_number(i)) == True:
            print(i,": is Fibonacci number")
        else:
            print(i,": is not Fibonacci number")

main()
