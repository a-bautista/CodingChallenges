'''
    Validate if a given string can be interpreted as a decimal number.

        Some examples:
        "0" => true
        " 0.1 " => true
        "abc" => false
        "1 a" => false
        "2e10" => true
        " -90e3   " => true
        " 1e" => false
        "e3" => false
        " 6e-1" => true
        " 99e2.5 " => false
        "53.5e93" => true
        " --6 " => false
        "-+3" => false
        "95a54e53" => false

    Note: It is intended for the problem statement to be ambiguous.
    You should gather all requirements up front before implementing one.
    However, here is a list of characters that can be in a valid decimal number:

    Numbers 0-9
    Exponent - "e"
    Positive/negative sign - "+"/"-"
    Decimal point - "."
'''


class Solution:
    def isNumber(self, s: str) -> bool:
        """
          :type s: str
          :rtype: bool
        """
        # define a DFA
        state = [{},
                 {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
                 {'digit': 3, '.': 4},
                 {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
                 {'digit': 5},
                 {'digit': 5, 'e': 6, 'blank': 9},
                 {'sign': 7, 'digit': 8},
                 {'digit': 8},
                 {'digit': 8, 'blank': 9},
                 {'blank': 9}]
        currentState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [3, 5, 8, 9]:
            return False
        return True


def main():
    valid_cases = ['3e7','+45']
    invalid_cases = ['111e','3e 8','e7','..1']
    solution = Solution()

    for v in invalid_cases:
        res = solution.isNumber(v)
        print('The case '+v+' is: '+str(res))

main()

'''
    Time complexity: O(N) where n is the number of chars in the string.
    Space complexity: O(1) because you are assigning the values to the dictionary.
'''