'''

Given two positive integers n and k.

A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order,
return the kth factor in this list or return -1 if n has less than k factors.

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.

'''

def KthFactorOfN(n, k):
    count =0
    for i in range(1, n+1):
        if n%i==0:
            count+=1
        if count == k:
            return i
    return -1


def main():
    sol = KthFactorOfN(12,5)
    print(sol)

main()

'''
    Time complexity: O(N)
    Space complexity: O(1)
'''