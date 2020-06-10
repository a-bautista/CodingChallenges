from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        groups = defaultdict(list)
        for s in strings:
            groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += s,
        return groups.values()

def main():
    solution = Solution()
    res = solution.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
    print(res)

main()

'''

    Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting 
    sequence.
    Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". 
    We can keep "shifting" which forms the sequence:

    "abc" -> "bcd" -> ... -> "xyz"


    To identify each group, compute the modulo 26 difference between each letter in a word with the first letter in it.
    Note: Originally the problem required each group to be sorted. Not anymore. I now added adapted solutions but kept 
    the old ones.
'''

# def groupStrings(self, strings: List[str]) -> List[List[str]]:
# 	hashmap = {}
# 	for s in strings:
# 		key = ()
# 		for i in range(len(s) - 1):
# 			circular_difference = 26 + ord(s[i+1]) - ord(s[i])
# 			key += (circular_difference % 26,)
# 		hashmap[key] = hashmap.get(key, []) + [s]
# 	return list(hashmap.values())