from time import time
from math import sqrt, pow

def main():
    start = time()
    myList = [20,40,60,80,100,120,140,160,180,200]
    operation2(myList)
    end_time = time()
    print(end_time-start)


def operation(myList):

    for n in myList:
        print(sqrt(n))
        print(pow(n,2))


def operation2(myList):

    for n in myList:
        print(sqrt(n))

    for n in myList:
        print(pow(n,2))


if "__main__" == __name__:
    main()

0.0009975433349609375
0.0010554790496826172