def decimalToBinary(N):
    # To store the binary number
    B_Number = 0
    cnt = 0
    while (N != 0):
        rem = N % 2
        c = pow(10, cnt)
        B_Number += rem * c
        N //= 2
        # Count used to store exponent value
        cnt += 1
    return B_Number


def decimal_to_binary_my_approach(num):
    res = []
    while num!=0:
        res.append(num%2)
        num = num // 2

    # manual reverse
    inverted = []
    for i in range(len(res)-1, -1,-1):
        inverted.append(res[i])

    print("".join(map(str, inverted)))
    res = int("".join(map(str, res[::-1])))
    return res

def main():
    num = 100
    dec_to_bin = decimal_to_binary_my_approach(4)
    print(dec_to_bin)

main()
