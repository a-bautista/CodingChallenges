class Solution:
    def addBinary(self, a, b):
        x = int(a, 2)
        y = int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

def main():
    solution = Solution()
    res = solution.addBinary('1111','101')
    print(res)

main()

"""
    
    Time complexity : O(N+M), where NNN and MMM are lengths of the input strings a and b.

    Space complexity : O(max(N,M)) to keep the answer.

"""