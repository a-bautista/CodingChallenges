'''
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    Example 1:

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:

    Input: n = 1
    Output: ["()"]

    You need to find out that 2 * n = number of parenthesis

    n = 2, then you have 2* 2 = 4 which will be the number of generated parenthesis
    (()) or ()()

'''

def solve(n):
    ans = []

    def backtrack(currentParenthesis, left, right):
        if 2*n == len(currentParenthesis):
            ans.append("".join(currentParenthesis))

        if left < n:
            currentParenthesis.append('(')
            backtrack(currentParenthesis, left + 1, right)
            currentParenthesis.pop()

        if right < left:
            currentParenthesis.append(')')
            backtrack(currentParenthesis, left, right +1)
            currentParenthesis.pop()

    backtrack([], 0, 0)
    return ans

def main():
    res = solve(2)
    print(res)

main()