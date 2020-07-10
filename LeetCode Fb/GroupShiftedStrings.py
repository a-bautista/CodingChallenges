'''
    Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

    "abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

'''
class Solution:
	def groupStrings(self, strings):
		hashmap = {}
		for s in strings:
			key = ()
			for i in range(len(s) - 1):
			# we subtract the adjacent letter - the previous letter and we add 26 and then % 26,so in this way we can create a circular reference as a key.
				circular_difference = 26 + ord(s[i+1]) - ord(s[i])
				# add the key to the tuple
				key += (circular_difference % 26,)
			# add the key to the hashmap and add the string
			hashmap[key] = hashmap.get(key, []) + [s]
		return list(hashmap.values())


def main():
	words = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
	solution = Solution()
	res = solution.groupStrings(words)
	print(res)

main()

'''
    Time complexity: O(mk) where m is the length of the list o strings and k is the longest string in the list.
    Space complexity: O(n) space in our hashmap
'''

