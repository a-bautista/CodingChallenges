class Solution:
    def addBinary(self, a, b):
        x = 0
        y = 0
        # convert from binary to decimal
        for i, c in enumerate(a):
            if c == '1':
                x+=(2**i)

        for i, c in enumerate(b):
            if c == '1':
                y+=(2**i)

        #x = int(a, 2)
        #y = int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

# class Solution:
#      def addBinary(self, a, b):
#          if len(a)==0: return b
#          if len(b)==0: return a
#          if a[-1] == '1' and b[-1] == '1':
#              return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
#          if a[-1] == '0' and b[-1] == '0':
#              return self.addBinary(a[0:-1],b[0:-1])+'0'
#          else:
#              return self.addBinary(a[0:-1],b[0:-1])+'1'


def main():
    solution = Solution()
    res = solution.addBinary('101','110')
    print(res)

main()

"""
    
    Time complexity : O(N+M), where NNN and MMM are lengths of the input strings a and b.

    Space complexity : O(max(N,M)) to keep the answer.

"""