'''
    Given a list of ip addresses, sort them in ascending order.
'''

from functools import cmp_to_key
def customComparator(a,b):
    octetsA = a.strip().split(".")
    octetsB = b.strip().split(".")

    if octetsA == octetsB:
        return 0

    elif octetsA[0] > octetsB[0]:
        return 1
    elif octetsA[0] < octetsB[0]:
        return -1

    elif octetsA[1] > octetsB[1]:
        return 1
    elif octetsA[1] < octetsB[1]:
        return -1

    elif octetsA[2] > octetsB[2]:
        return 1
    elif octetsA[2] < octetsB[2]:
        return -1

    elif octetsA[3] > octetsB[3]:
        return 1
    elif octetsA[3] < octetsB[3]:
        return -1



def main():
    ips = ['10.10.5.10',
           '40.5.4.10',
           '11.10.15.20',
           '10.9.10.5',
           '20.20.20.5',
           '10.0.5.8']
    res_sorted = sorted(ips, key=cmp_to_key(customComparator))
    print(res_sorted)

main()

'''
    https://stackoverflow.com/questions/29726919/how-does-a-python-custom-comparator-work
    https://stackoverflow.com/questions/16362744/how-does-pythons-cmp-to-key-function-work
'''