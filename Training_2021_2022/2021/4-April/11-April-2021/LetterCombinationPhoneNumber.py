'''
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number 
    could represent. Return the answer in any order.

    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does 
    not map to any letters.

    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    Input: digits = "2"
    Output: ["a","b","c"]

    Input: digits = ""
    Output: []

'''

class Solution:
    def solve(self, digits):
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def dfs(combination, nextDigit):
            if len(nextDigit) == 0:
                # combination is done
                output.append(combination)
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[nextDigit[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    dfs(combination + letter, nextDigit[1:])

        output = []
        if digits:
            dfs("", digits)
        return output

def main():
    digits = '23'
    solution = Solution()
    res = solution.solve(digits)
    print(res)

main()

'''
    Time complexity: O((3**N)*(4**N))) where n is the number of digits in the input that maps to 3 letters 
    and M is the input of digits that maps to 4 letters
    Space complexity: O((3**N)*(4**N)))
'''