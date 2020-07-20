def toHex(num):
    if num == 0: return '0'
    mp = '0123456789abcdef'  # like a map
    ans = ''
    # we iterate by 8 because 1 byte has 8 bits
    for i in range(8):
        # the line from below is equivalent to n = num % 16
        n = num & 15  # this means num & 1111b (15 = 1111 in binary)
        #n = num % 16
        c = mp[n]  # get the hex char
        ans = c + ans
        # the line from below is equivalent to num = num // 16
        #num = num // 16
        num = num >> 4
    return ans.lstrip('0')  # strip leading zeroes because we won't need them

def main():
    num = 26
    res = toHex(num)
    print(res)

main()

'''
    Time complexity: O(n)
    Space complexity: O(1)
'''

