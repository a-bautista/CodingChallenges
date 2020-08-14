'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and
empty spaces .
The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7


'''

class Solution:
    def calculate(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                # convert the string number to int
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        # add all the values of the sum (positive and negative signs)
        return sum(stack)


def main():
    s = "3+2*2"
    solution = Solution()
    res = solution.calculate(s)
    print(res)


main()