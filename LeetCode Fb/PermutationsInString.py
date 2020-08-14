'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one
of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


'''

def checkInclusion(s1, s2):
    # generate two lists where the first one will contain all values in the first string with a 1 and the second
    # list will be used to reference our window
    l1 = [0] * 26
    l2 = [0] * 26
    for x in s1:
        # add the value 1 once you find a char in s1
        l1[ord(x) - ord('a')] += 1

    for i in range(len(s2)):
        # add the value 1 once you find a char in s2
        l2[ord(s2[i]) - ord('a')] += 1
        # shrink the size of the window to the same size of the s1, so we can have
        # these two references
        # [1,1,0,0,0,0,...]
        # [1,1,0,0,0,0,...]
        # once we have this then we know the substring is contained in the l2
        if i >= len(s1):
            l2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        # once you find that both lists are the same then you can indicate that s1 chars is contained in s2 string.
        if l1 == l2:
            return True
    return False

def main():
    s1 = "ab"
    s2 = "eidbaooo"
    res = checkInclusion(s1, s2)
    print(res)

main()

'''
    Time complexity: O(N) where N is the number of chars in the longest string.
    Space complexity: O(1) because we know we will need 26 spaces. 
'''