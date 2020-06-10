"""
    In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
    The order of the alphabet is some permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if
    the given words are sorted lexicographicaly in this alien language.
"""

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic = {}
        new_words = []
        # create the dictionary with the letter and order numbering {'h':0, 'e':1}
        # O(N) because I depend on the number of elements in order
        for i, ch in enumerate(order):
            dic[ch] = i

        # for each word in the words list, get the number of each letter in the dictionary
        # O(k) where k is each letter
        for w in words:
            new = []
            for c in w:
                new.append(dic[c])
            new_words.append(new)

        # O(mn) for comparing each letter in arrays
        # compare each letter from the two lists that contain the ordering of each letter
        for w1, w2 in zip(new_words, new_words[1:]):

        # if you find that the ordering of a letter in word1 is greater than word2, then the ordering is incorrect
            if w1 > w2:
                return False
        return True

def main():
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    solution = Solution()
    res = solution.isAlienSorted(words, order)
    print(res)

main()

"""
    Time complexity: O(mn)
    Space complexity: O(mn)
"""