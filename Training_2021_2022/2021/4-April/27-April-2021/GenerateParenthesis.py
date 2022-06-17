'''
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    Example 1:

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:

    Input: n = 1
    Output: ["()"]
 
'''

def solve(n):
    stack = []

    def backtrack(container, left, right):
        if len(container)==2*n:
            # you don't need the list(container) because with "".join() we are getting the results
            stack.append("".join(container))
        
        # keep adding the left parenthesis because we still have room for them
        if left < n:
            container.append("(")
            backtrack(container, left+1, right)
            # backtrack
            container.pop()

        # we need to add closing parenthesis
        if right < left:
            container.append(")")
            backtrack(container, left, right+1)
            # backtrack
            container.pop()

    backtrack([], 0, 0)
    return stack

def main():
    res = solve(3)
    print(res)

main()