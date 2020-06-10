'''Given a string containing digits from 2-9 inclusive, return
all possible letter combinations that the number could represent.

Input: "23" where 2 contains abc and 3 contains def
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_ = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []

        def make_combinations(i, cur):
            if i == len(digits):
                if len(cur) > 0:
                    result.append(''.join(cur))
                return
            for ch in map_[digits[i]]:
                cur.append(ch)
                make_combinations(i + 1, cur)
                cur.pop()

        make_combinations(0, [])

        return result


def main():
    solution = Solution()
    res = solution.letterCombinations("23")
    print(res)

main()