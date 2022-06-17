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

def removeDuplicateLetters(s):
    stack = []
    # this lets us keep track of what's in our solution in O(1) time
    seen = set()
        # this will let us know if there are no more instances of s[i] left in s
    last_occurrence = {c:i for i, c in enumerate(s)}
    
    for i, c in enumerate(s):
        # we can only try to add c if it's not already in our solution
        # this is to maintain only one of each character
        if c not in seen:
            # i < last_occurrence[stack[-1]] indicates that the current index letter position
            # is bbehind the last occurrence of the last letter that is contained in the stack
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.discard(stack.pop())
            seen.add(c)
            stack.append(c)
    return ''.join(stack)

def main():
    s= "bcabc"
    res = removeDuplicateLetters(s)
    print(res)

main()