'''
    Given 2 strings, check to see if they are anagrams.

    "public relation" is an anagram of "crap built of lies".

'''

def solve(a1, a2):

    # edge case
    if len(a1) <=0 or len(a2)<=0:
        return -1

    # clean the words
    a1 = a1.replace(" ","")
    a2 = a2.replace(" ","")

    main_dict = {}
    for i in range(len(a1)):
        if a1[i] not in main_dict:
            main_dict[a1[i]] =1
        else:
            main_dict[a1[i]] += 1

    for j in range(len(a2)):
        if a2[j] in main_dict:
            main_dict[a2[j]] -=1
        if a2[j] not in main_dict:
            main_dict[a2[j]] = 1

    for k in main_dict:
        if main_dict[k]!=0:
            return False

    return True


def main():
    a1= "public relations"
    a2 = "crap built on lies"
    print(solve(a1,a2))

main()

'''
    Time complexity: O(N)
    Space complexity: O(1)
'''