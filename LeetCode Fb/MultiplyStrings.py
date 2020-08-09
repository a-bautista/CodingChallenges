"""
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
    also represented as a string.

    Example 1:

        Input: num1 = "2", num2 = "3"
        Output: "6"

    Example 2:

        Input: num1 = "123", num2 = "456"
        Output: "56088"

"""

class Solution:

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # create a list to keep the results
        res = [0] * (len(num1) + len(num2))

        # multiply the numbers by reversing them
        for i, v1 in enumerate(reversed(num1)):
            for j, v2 in enumerate(reversed(num2)):
                # convert the numbers to an int value by subtracting the char values
                int1 = ord(v1) - ord('0')
                int2 = ord(v2) - ord('0')

                res[i + j] += int1 * int2 # multiply the numbers
                res[i + j + 1] += res[i + j] // 10 # bring out carry number and put it on the right
                res[i + j] %= 10 # in the current position, store the number without the carry

        # in case you have found a zero value at the end, remove it
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        # join all the values and then invert them to get the correct number
        return ''.join(str(v) for v in res)[::-1]

def main():
    nums1 = '123'
    nums2 = '456'
    solution = Solution()
    res = solution.multiply(nums1, nums2)
    print(res)

'''
    Time complexity: O(M*N)
    Space complexity: O(N)
'''



main()