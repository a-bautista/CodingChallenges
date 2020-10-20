'''
    Given a number N, swap the two nibbles in it and find the resulting number.
    Example 1:

    Input:
    N = 100
    Output:
    70
    Explanation:
    100 in binary is 01100100, two nibbles are (0110) and (0100)
    If we swap the two nibbles, we get 01000110 which is 70 in decimal
'''

class Solution:
    def swapNibbles(self, N):
        bin_num = str(self.helper_convertDecToBin(N))

        if  len(bin_num) < 9:
            bin_num = bin_num.zfill(8-len(bin_num)+len(bin_num))

        first_portion, second_portion = bin_num[:4], bin_num[4:]
        swapped = second_portion + first_portion
        return self.helper_convertBinToDec(swapped[::-1])


    # def helper2_convert_bin_to_decimal(self, N):
    #     dec, res, i = 0, 0, 0
    #     while N!=0:
    #         dec = N%10
    #         res += dec * pow(2,i)
    #         N = N//10
    #         i += 1
    #     print(res)
    #     return res

    def helper_convertDecToBin(self, N):
        res = []
        while N!=0:
            residual = N % 2
            res.append(str(residual))
            N //=2
        # res = res.reverse() this throws a None:
        print(res[::-1])
        return "".join(res)[::-1]

    def helper_convertBinToDec(self, N):
        ''' The number N is already reversed. '''
        res = 0
        for i in range(len(N)-1, -1,-1):
            if N[i]!='0':
                res += 2**i
        return res

def main():
    sol = Solution()
    res = sol.swapNibbles(20)
    print(res)

main()