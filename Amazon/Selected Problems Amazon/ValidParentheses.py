"""

    Time complexity is O(N) and space complexity is O(N).

    We can use a a set as a stack data structure to store the corresponding values of parentheses.
    1. Create a hash table with the ending brackets and assign them to the initial brackets.
    2. For every character in the expression s, verify if the char is an ending bracket or open-ended bracket.
        if it is an open-ended bracket then add that bracket in a list (stack)
        else,
        then pop the previous element that contained the list to establish that open and ended values were found.
    3. if there's not an ending char in the stack

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack