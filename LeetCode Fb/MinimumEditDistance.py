'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

'''

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)

        # if one of the strings is empty
        if n * m == 0:
            return n + m

        # array to store the conversion history
        # where each list represent the letters of word1 and the internal values represent the letters of word2
        # d = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        d = [[0] * (m + 1) for _ in range(n + 1)]

        # init boundaries
        # d = [[0, 1, 2, 3], [1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [4, 0, 0, 0], [5, 0, 0, 0]]
        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j

        # DP compute
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = d[i - 1][j] + 1
                # down is computed only when we have the same letters
                down = d[i][j - 1] + 1
                left_down = d[i - 1][j - 1]
                # if letter are different then we add 1 to left_down this value will be taken in the min
                # this applies only when letters are different
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                d[i][j] = min(left, down, left_down)

        # the result will be given at the very end of the array
        return d[n][m]


def main():
    word1 = "horse"
    word2 = "ros"
    solution = Solution()
    res = solution.minDistance(word1, word2)
    print(res)

main()

'''
    Time complexity: O(mn)
    Space complexity: O(mn)
'''