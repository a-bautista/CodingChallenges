"""
    Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be
    segmented into a space-separated sequence of one or more dictionary words.

    Note:
        The same word in the dictionary may be reused multiple times in the segmentation.
        You may assume the dictionary does not contain duplicate words.

"""

class Solution:
    def wordBreak(self, s, wordDict):
        #dp = [False] * len(s)
        dp = [True] + [False] * len(s) # add a True and then add the rest of the list as False
        #for i in range(0, len(s)-1):
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[:i].endswith(word):
                    # |= means bitwise or, i.e.,
                    # when i=4 then dp[i] or dp[i-len(word)] means
                    # dp[4] = False
                    # dp[4-len(word)] word = leet  then dp[4-4] = dp[0] = True
                    # dp[0] or dp[4] = True or False = True
                    dp[i] |= dp[i-len(word)]
        # return the last element
        print(dp)
        return dp[-1]


def main():
    s = 'facebookbook'
    wordDict = ['book']
    solution = Solution()
    res = solution.wordBreak(s, wordDict)
    print(res)

main()

"""
    Time complexity: 
        O(s*k) first loop iterates s times while second loop iterates k times and conditional is constant time.
    Space complexity:
        O(s*k) maybe?
"""