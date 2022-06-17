'''
    You are given a string word that consists of digits and lowercase English letters.

    You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34". Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".

    Return the number of different integers after performing the replacement operations on word.

    Two integers are considered different if their decimal representations without any leading zeros are different.

    Example 1:

    Input: word = "a123bc34d8ef34"
    Output: 3
    Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.
    Example 2:

    Input: word = "leet1234code234"
    Output: 2
    Example 3:

    Input: word = "a1b01c001"
    Output: 1
    Explanation: The three integers "1", "01", and "001" all represent the same integer because
    the leading zeros are ignored when comparing their decimal values.
'''

def numDifferentIntegers(word):
    out = ''
    for char in word:
        if char.isdigit():
            out = out + char
        else:
            out = out + ' '
    
    out = out.split(' ')
    # clean the spaces
    out_clean = []
    print(out)
    for val in out:
        if val!='':
            out_clean.append(int(val))
    return len(set(out_clean))
    

def main():
    word = "a123bc34d8ef34"
    word2= "a1b01c001"
    res = numDifferentIntegers(word)
    print(res)


main()