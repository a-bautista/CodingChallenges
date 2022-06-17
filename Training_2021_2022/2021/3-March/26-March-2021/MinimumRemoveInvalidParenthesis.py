"""
    Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
    parentheses string is valid and return any valid string.

    Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

    Example 1:

        Input: s = "lee(t(c)o)de)"
        Output: "lee(t(c)o)de"
        Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

    Example 2:

        Input: s = "a)b(c)d"
        Output: "ab(c)d"
    
    # holds the parenthesis index
    stack = []
    
    # contains the indexes that will be removed in case the stack is empty
    set()

    make a union of the stack and set, so you have all the indexes that contain the parenthesis
    that do not match its pair
"""
def solve(str1):
    stack = []
    indexesToRemove = set()
    res = ""
    for i, val in enumerate(str1):

        # disregard the letters, just continue onto the next letter
        if val not in "()":
            continue

        if val == '(':
            stack.append(i)
        elif not stack:
            indexesToRemove.add(i)
        else:
            stack.pop()

    # union of stack and set
    indexesToRemove = indexesToRemove.union(set(stack))

    # string builder to concatenate only the letters and parenthesis that match
    for i, val in enumerate(str1):
        if i not in indexesToRemove:
            res+=val
    return res

def main():
    s = "lee(t(c)o)de)"
    res = solve(s)
    print(res)
    #Input: s = "lee(t(c)o)de)"
    #Output: "lee(t(c)o)de"

main()