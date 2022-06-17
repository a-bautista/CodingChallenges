'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.


Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            elif stack:
                if s[i] == ")" and stack[-1]=="(":
                    stack.pop()
                elif s[i]=="]" and stack[-1]=="[":
                    stack.pop()
                elif s[i]=="}" and stack[-1]=="{":
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return True if len(stack)==0 else False