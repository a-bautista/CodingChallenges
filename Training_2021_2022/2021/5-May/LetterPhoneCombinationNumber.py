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
        res = []
        phone = {
                '2': ["a", "b", "c"],
                '3': ["d","e", "f"],
                '4': ["g", "h", "i"],
                '5': ["j", "k", "l"],
                '6': ["m", "n", "o"],
                '7': ["p", "q", "r", "s"],
                '8': ["t", "u", "v"],
                '9': ["w", "x", "y", "z"]             
                }

        def dfs(digits, combination):
            if len(digits)==0:
                res.append(combination)
            else:
                for letter in phone[digits[0]]:
                    # append the letter
                    combination+= letter
                    # current digit
                    dfs(digits[1:], combination)
                    # backtrack
                    combination = combination[:-1]
        dfs(digits, "")    
        return res

def main():
    solution = Solution()
    res = solution.solve('23')
    print(res)

main()
    