def binary_to_decimal_optimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal += dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

# time complexity: O(N)
# space complexity: O(1)

def binary_to_decimal_traditional(binary):
    res = 0
    str_binary = str(binary)[::-1]
    for i in range(len(str_binary)-1,-1,-1):
        if str_binary[i]!='0':
            res += 2**i
    return res

# time complexity: O(n*log(n)) due to the reversal
# space complexity: O(1)

def main():
    num = 100
    num2 = 1000
    res = binary_to_decimal_optimal(num)
    res2 = binary_to_decimal_traditional(num2)
    print(res)
    print(res2)

main()