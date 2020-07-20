class Solution(object):
    def myAtoi(self, str: str) -> int:
        # define your min and max values
        intMax = 2147483647
        intMin = -2147483648

        # remove the white spaces
        str = str.strip()

        if not str:
            return 0

        # determine the sign either positive or negative
        sign, i = 1, 0
        if str[i] == "+":
            # go onto the next value of the given string
            i += 1
        elif str[i] == "-":
            sign = -1
            # go onto the next value of the given string
            i += 1

        # use num to store the integer number
        num = 0

        while i < len(str):
            # if the char is not digit then break the loop
            if not str[i].isdigit():
                break

            # use the ord to convert from string to numeric by using ord('number') - ord('0')
            # use the num * 10 to take into account the number of times we increase 10
            num = num * 10 + ord(str[i]) - ord('0')
            if num > intMax:
                break
            # go onto the next char
            i += 1
        # stay in the boundaries of the min and max values
        return min(max(sign * num, intMin), intMax)

def main():
    s = '  4442'
    solution = Solution()
    res = solution.myAtoi(s)
    print(res)

main()

'''
    Time complexity: O(N)
    Space complexity: O(1)
'''