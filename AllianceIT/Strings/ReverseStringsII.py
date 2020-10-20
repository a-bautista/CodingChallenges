"""
Reverse only Letters

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"

Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

"""
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s_list = list(S)
        left = 0
        right = len(S)-1
        #invalid_chars = {"-","+","=","?","!","1"}
        big_invalid_chars = { chr(x) for x in range(32,64)}
        small_invalid_chars = { chr(x) for x in range(91,96)}
        invalid_chars = big_invalid_chars.union(small_invalid_chars)

        while left <= right:
            if s_list[left] in invalid_chars:
                left+=1
            elif s_list[right] in invalid_chars:
                right-=1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left +=1
                right -=1
        return "".join(s_list)

def main():
    solution = Solution()
    res = solution.reverseOnlyLetters("Test1ng-Leet=code-Q!")
    print(res)

main()

'''
acx-by
Input: "ab-cd"
Output: "dc-ba"
Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

'''