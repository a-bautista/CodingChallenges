'''
    Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. 
    Also two strings X and Y are similar if they are equal.

    For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, 
    but "star" is not similar to "tars", "rats", or "arts".

    Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" 
    and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in 
    the group if and only if it is similar to at least one other word in the group.

    We are given a list strs of strings where every string in strs is an anagram of every other string in strs. 
    How many groups are there?
 
    Example 1:

    Input: strs = ["tars","rats","arts","star"]
    Output: 2

'''
from collections import defaultdict
def solve(words):

    res = dict([])
    #res = defaultdict([])
    for word in words:
        
        temp = [0]*26
        for letter in word:
            temp[ord(letter)-ord('a')]+=1

        # defaultdict       
        # res[tuple(temp)].append(word)
        if tuple(temp) not in res:
            res[tuple(temp)] = []
        res[tuple(temp)].append(word)

    return res.values()        

def main():
    words = ["tars","rats","arts","star"]
    res = solve(words)
    print(res)

main()

'''
    1. Retrieve each word from the list
    2. Create a temp list of 0s. This array will be the key in the dict to determine if the words are anagrams. 
        2.1. We will do ord(char)-ord('a'), this will indicate position in the alphabet, then will add + 1 for the given word
        2.2. ate, eat --> [1,0,0,0,1,0,0,0,....]
    3. Use this list for the key in the dictionary.
    4. Return the the count of groups in the dictionary
'''