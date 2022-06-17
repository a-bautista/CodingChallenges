'''
    A string S of lowercase English letters is given. We want to partition this string into as many parts as possible 
    so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
 
    Example 1:

    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

    Note:

        S will have length in range [1, 500].
        S will consist of lowercase English letters ('a' to 'z') only.
'''
#from collections import Counter
def solve(s):
    rightmost = {letter: index for index, letter in enumerate(s) }
    left, right = 0, 0
    res = []
    for i, letter in enumerate(s):
        # find the last time the first letter appeared and once the index is equal to that letter
        # then you will know that you have hit the last occurrence of it, so mark it as a partition
        right = max(right, rightmost[letter])
        
        if i==right:
            res.append(right - left +1)
            left = right + 1
    return res

def main():
    s = "ababcbacadefegdehijhklij"
    res = solve(s)
    print(res)

main()