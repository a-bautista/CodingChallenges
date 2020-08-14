'''

Given a string, determine if a permutation of the string could form a palindrome.

'''
from collections import Counter
class Solution:
    def canPermutePalindrome(self, s):
        #dic = {}
        dic = Counter(s)
        #for item in s:
        #    dic[item] = dic.get(item, 0) + 1
        # return sum(v % 2 for v in dic.values()) < 2

        count1 = 0
        for val in dic.values():
            # basically if aaba which has 3 'a' then when mod by 2 will give 1 and when you do the b then you will get another 1, so this is not palindrome
            if val % 2 == 1:
                count1 += 1
            if count1 > 1:
                return False
        return True

def main():
    input = 'aaba'
    solution = Solution()
    res = solution.canPermutePalindrome(input)
    print(res)

main()

'''
    Time complexity: O(N) because we traverse over the given string s once.
    Space complexity: O(1)
'''