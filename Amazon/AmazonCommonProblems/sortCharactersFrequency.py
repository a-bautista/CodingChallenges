'''
    Given a string, sort it in decreasing order based on the frequency of characters.

    Example 1:

    Input:
        "tree"

    Output:
        "eert"

    Explanation:
        'e' appears twice while 'r' and 't' both appear once.
        So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


    Input:
        "cccaaa"

    Output:
        "cccaaa"

    Explanation:
        Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
        Note that "cacaca" is incorrect, as the same characters must be together.


    Input:
        "Aabb"

    Output:
        "bbAa"

    Explanation:
        "bbaA" is also a valid answer, but "Aabb" is incorrect.
        Note that 'A' and 'a' are treated as two different characters.

    Req:

        Display the letters from the max freq to the lowest.
        In case of a tie between letters, display them from in a descending order (a - z)
        In case of a single upper case letter, display it at the end.
        There is no limit to the array of letters.
        Want to keep it in the O(n) and avoid O(n)**2

        c c c a a a

        first I want to count the unique values in the array and store them in a dict or maybe a heap max,
        to always have the max values at the top. (it is a hash map because of letters, heap will be used to always keep the max
        value, it could be possible to implement it, though.
        then I can convert the dict into a list ordered from the highest to the lowest value of letter count.

        approach was good but lack of ability to know the data structure that you needed
'''

import collections

def main():
    s1 = 'cccaaa'
    s2 = 'Aabb'
    res = frequencySort(s2,s2)
    print(res)

def frequencySort(self, s: str) -> str:
    # Count up the occurances.

    # Counter creates a hash map
    # Assgning each letter
    counts = collections.Counter(s)

    print(counts)
    # Build up the string builder to assign individual values and keep the complexity in O(1) for each assignation and
    # be always in O(n)

    string_builder = [] # append the values in the
    for letter, freq in counts.most_common(): #  this creates a type of sort
        # letter * freq makes freq copies of letter.
        # e.g. "a" * 4 -> "aaaa"
        string_builder.append(letter * freq)
    return "".join(string_builder)

if __name__ == '__main__':
    main()

'''
   Let n be the length of the input String and k be the number of unique characters in the String.

   We know that k≤n, because there can't be more unique characters than there are characters in the String. 
   We also know that k is somewhat bounded by the fact that there's only a finite number of characters in Unicode (or ASCII, 
   which I suspect is all we need to worry about for this question).

   There are two ways of approaching the complexity analysis for this question.
   We can disregard k, and consider that in the worst case, k = n (unique characters are all different)
   
   So, putting the characters into the HashMap has a cost of O(n), because each of the nnn characterss must be put in, and putting
   each in is an O(1) operation.
   
   Sorting the HashMap keys has a cost of O(k log() k) because there are k keys and this is the standard cost of sorting. 
   If only using n, then it's O(n log() n). For the previous question, the sort was carried out on n items, not k, so was 
   possibly a lot worse.
   
   Traversing over the sorted keys and building the String has a cost of O(n), as n characters must be inserted.
   Therefore, if we're only considering n, then the final cost is O(n log() n). 
   
   
   Space Complexity : O(n).
   The HashMap uses O(k) space.
   However, the StringBuilder at the end dominates the space complexity, pushing it up to O(n), 
   as every character from the input String must go into it. Like was said above, 
   it's impossible to do better with the space complexity here.


    https://leetcode.com/problems/sort-characters-by-frequency/solution/

'''