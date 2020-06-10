"""
    Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to
    construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

    Note:

        The same word in the dictionary may be reused multiple times in the segmentation.
        You may assume the dictionary does not contain duplicate words.

    Example 1:

        Input:
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        Output:
        [
          "cats and dog",
          "cat sand dog"
        ]
"""

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):

        # verify if the word is already contained in the dict
        if s in memo:
            return memo[s]

        if not s:
            return []

        res = []
        # for each word in wordDict, do an iteration
        for word in wordDict:
            # if the string doesn't start with the word in wordDict then continue
            if not s.startswith(word):
                continue
            # if the word in wordDict is the same as what is left in s then append the word to the result
            if len(word) == len(s):
                res.append(word)
            else:
                # when the word in wordDict starts in s string
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                # append the word that
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res


def main():
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    #s = "parisabellelle"
    #wordDict = ["paris", "isabelle", "isa", "elle", "el"]
    solution = Solution()
    res = solution.wordBreak(s, wordDict)
    print(res)


main()


'''
    Time complexity: The word length in a word of wordDict is E(k), 
                     s length is n, the number of words in wordDict is size m. 
                     The recursion depth is n/E(k) and each recursion has m branches,
                     so time complexity might be O(m^(n/E(k)).
    Space complexity: O(m) for the wordDict, O(n) for the len(s) and O(mn)
    

'''