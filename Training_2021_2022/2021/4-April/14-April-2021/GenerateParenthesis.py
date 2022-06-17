'''
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    Example 1:

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:

    Input: n = 1
    Output: ["()"]
 
'''

def generate_parenthesis(n):
    ans = []

    def backtrack(temp, left, right):
        if len(temp) == 2 * n:
            # you are creating a new list here otherwise when you do a pop of the temp variable then this will
            # affect the result of ans
            ans.append("".join(temp))
            return 
        
        if left < n:
            temp.append("(")
            backtrack(temp, left + 1, right)
            temp.pop()

        if right < left:
            temp.append(")")
            backtrack(temp, left, right + 1)
            temp.pop()

    backtrack([], 0, 0)
    return ans

def main():
    res = generate_parenthesis(2)
    print(res)

main()