'''
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

    Time: O(M*N)
    Space: O(M)

'''

def longestCommonPrefix(m):
    if not m: return ''
    #since list of string will be sorted and retrieved min max by alphebetic order
    s1 = min(m)
    s2 = max(m)

    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i] #stop until hit the split index
    return s1

def main():

    s = ["dog","racecar","car"]
    res = longestCommonPrefix(s)
    print(res)

main()