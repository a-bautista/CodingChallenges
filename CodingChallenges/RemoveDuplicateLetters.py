'''

    Given a string s, remove duplicate letters so that every letter appears once and only once.
     You must make sure your result is the smallest in lexicographical order among all possible results.

    Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

    Example 1:

    Input: s = "bcabc"
    Output: "abc"

    Example 2:

    Input: s = "cbacdcbc"
    Output: "acdb"

'''


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        # this lets us keep track of what's in our solution in O(1) time
        seen = set()

        # where was the last occurrence of the letter c in the string s
        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):

            # we can only try to add c if it's not already in our solution
            # this is to maintain only one of each character
            if c not in seen:
                # if the last letter in our solution:
                #    1. exists
                #    2. is greater than c so removing it will make the string smaller
                #    3. it's not the last occurrence
                # we remove it from the solution to keep the solution optimal
                # i < last_occurrence[stack[-1]] indicates that if the current index of letter c
                # is less than the last occurrence of the letter contained in the stack then it means
                # we still have more of the contained letters in the stack in the s string
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)

def main():
    s = "cbacdcbc"
    s1 = "aaaaaba"
    sol = Solution()
    print(sol.removeDuplicateLetters(s1))

main()

'''
    Time complexity: O(N)
    Space complexity: O(1)
'''