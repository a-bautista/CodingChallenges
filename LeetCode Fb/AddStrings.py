'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []

        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        # I take each number one by one and convert it to an int with ord (we only take from 0 - 9)
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1 -= 1
            p2 -= 1

        if carry:
            res.append(carry)

        return ''.join(str(x) for x in res[::-1])


def main():
    solution = Solution()
    res = solution.addStrings("14","19")
    print(res)


main()

'''


    Time Complexity: O(max(N1,N2)) where N1​ and N2​ are length of nums1 and nums2. Here we do max⁡(N1,N2)\max(N_1, N_2)max(N1​,N2​) iterations at most.
    Space Complexity: O(max(N1,N2)) because the length of the new string is at most max⁡(N1,N2)+1\max(N_1, N_2) + 1max(N1​,N2​)+1.

'''