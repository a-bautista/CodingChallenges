# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         c = 0
#         while n:
#             n &= n - 1
#             c += 1
#         return c

# bin(number).count('1')
# Brian Kernighan’s Algorithm
# You have the number 6 and you want to count the number of 1s in binary.

# 6 in binary = 110
# 5 in binary = 101

# 6 - 5 = 1
# 110 and 101 = 100


# 4 in binary = 100
# 3 in binary = 011


# 2 in binary = 010
# 1 in binary = 001

# 1 - 1 = 0
# 01 and 01 = 01

def solve(n):

  c = 0
  while n:
    n &= n - 1
    c +=1
  return c

def main():
  num = 6
  res = solve(num)
  print(res)

main()