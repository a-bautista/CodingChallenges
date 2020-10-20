class Solution:
    def solve(self, number, kbit):
        return (1<<kbit) | number

def main():
    solution = Solution()
    res = solution.solve(10,2)
    print(res)

main()


'''
    Given a number N and a value K. From the right, set the Kth bit in the binary 
    representation of N. The position of Least Significant Bit(or last bit) is 0, 
    the second last bit is 1 and so on. 
'''