'''
    A string s is called good if there are no two different characters in s that have the same frequency.

    Given a string s, return the minimum number of characters you need to delete to make s good.

    The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

    

    Example 1:

    Input: s = "aab"
    Output: 0
    Explanation: s is already good.

    Example 2:

    Input: s = "aaabbbcc"
    Output: 2
    Explanation: You can delete two 'b's resulting in the good string "aaabcc".
    Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

    Example 3:

    Input: s = "ceabaacb"
    Output: 2
    Explanation: You can delete both 'c's resulting in the good string "eabaab".
    Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

    Algo
    Collect the frequency of letters in s in a frequency table. 
    Examine the frequencies from highest to lowest. If a frequency has been seen, lower it by 
    one by reducing its character. Repeat the operation until all frequencies are unique (possibly 
    removing some characters completely).

'''
from collections import Counter
def solve(s):
    freq = Counter(s)    
    res = 0
    seen = set()
    for k in freq.values(): 
        while k in seen: 
            k -= 1 
            res += 1
        if k: seen.add(k)
    return res

def main():
    s ="aaabbbcc"
    res = solve(s)
    print(res)

main()