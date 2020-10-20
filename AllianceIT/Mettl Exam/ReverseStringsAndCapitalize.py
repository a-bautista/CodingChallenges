'''

From hackerrank.
https://www.hackerrank.com/contests/codejam/challenges/reverse-words


Reverse the words in a string and capitalize the first letter of each reversed word, preserving the capitalization in the original stri. For eg: "Hello World" would be transformed to "OlleH DlroW".
Input

The first line of input would be the number of test cases followed by each string in a line.
Sample input

1
Hello World

'''

class Solution:
    def solve(self, s):
        s_tup = tuple(s.split(" "))
        res = []

        for i, val in enumerate(s_tup):
            temp = val[:-1]+val[-1:].upper()
            res.append(temp[::-1])
        return ' '.join(res)

def main():
    s1 = 'Hello World'
    s2 = 'A Good question'
    s3 = 'I am mad'

    solution = Solution()

    res1 = solution.solve(s1)
    res2 = solution.solve(s2)
    res3 = solution.solve(s3)

    print(res1)
    print(res2)
    print(res3)

main()