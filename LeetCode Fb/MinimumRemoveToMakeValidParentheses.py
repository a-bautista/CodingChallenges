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
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            # if you find a char (abcd.....z) then continue
            if c not in "()":
                continue
            # when you add a ( then add it to the stack
            if c == "(":
                stack.append(i)
            # if the stack is empty and you find a ')' then add the index
            # of that parenthesis
            elif not stack:
                indexes_to_remove.add(i)
            # remove the closing parenthesis ')'
            else:
                stack.pop()

        # this line is used to join the parenthesis that were left
        # in the stack with the indexes_to_remove
        indexes_to_remove = indexes_to_remove.union(set(stack))
        string_builder = []

        # start getting all the chars of the string except the char with the
        # closing index parenthesis
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)

def main():
    s = 'L(ee)(t(()co)d))e'
    s1 = 'a)b(c)d'
    s2 = '))(('
    s3 = '(a(b(c)d)'
    solution = Solution()
    res = solution.minRemoveToMakeValid(s1)
    print(res)

main()

"""
    Time complexity : O(n), where nnn is the length of the input string.
    Space complexity : O(n), where nnn is the length of the input string.
"""