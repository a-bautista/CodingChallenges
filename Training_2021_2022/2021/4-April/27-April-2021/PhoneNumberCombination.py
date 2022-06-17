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
    def solve(self, nums):
        phone = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t', 'u', 'v'],
            '9': ['w','x','y','z']
        }

        output = []
        def rec(combination, digits):
            if len(digits)==0:
                output.append(combination)
            else:
                # for each letter from the current number do a recursive call
                for letter in phone[digits[0]]:
                    # combination+= letter will continue adding the letters unless you do a backtrack
                    combination+= letter
                    # combination + letter just keeps the current appended letters (ad, ae, af) and this is a very elegant way of backtrack
                    # without explicitly defining it
                    rec(combination, digits[1:])
                    # backtrack of the string: get all the string except the last one
                    combination = combination[:-1]
        rec("", nums)
        return output

def main():
    solution = Solution()
    res = solution.solve('23')
    print(res)

main()

