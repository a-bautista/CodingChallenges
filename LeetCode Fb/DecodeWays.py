'''
    A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

    Given a non-empty string containing only digits, determine the total number of ways to decode it.

    Example 1:

    Input: "12"
    Output: 2
    Explanation: It could be decoded as "AB" (1 2) or "L" (12).

    Example 2:

    Input: "226"
    Output: 3
    Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

    Limitations:
        Given 01 then you return 0 because there's not any mapping between 0 and the alphabet.
        Given "" then you return 1.
        Given "12345" you decode from left to right.

        "1" is mapped to a and "12" is mapped to l then you have "345".

        Given "27345" then you have

        "2" is mapped to b then you have "7345".


Approach: We generate a bottom up DP table.

The tricky part is handling the corner cases (e.g. s = "30").

Most elegant way to deal with those error/corner cases, is to allocate an extra space, dp[0].

Let dp[ i ] = the number of ways to parse the string s[1: i + 1]

For example:
s = "231"
index 0: extra base offset. dp[0] = 1
index 1: # of ways to parse "2" => dp[1] = 1
index 2: # of ways to parse "23" => "2" and "23", dp[2] = 2
index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2

'''

class Solution:
    def decode(self, s):
        if not s:
            return 0

        '''
        12312
        ^
        1 way
        
        [1,1,0,0,0,0]
        
        12312
         ^
        2 ways because we have 12
        
        [1,1,2,0,0,0]
        
        
        12312
          ^
        3 ways because we have 1 and 23, 12 and 3, 1 and 2 and 3
        
        [1,1,2,3,0,0]
        
        12312
           ^
        1 way to decode the 1 because we cannot have the 31, so 
        we add it to the current ways, we have 
        1 and 23 and 1, 12 and 3 and 1, 1 and 1 and 2 and 3.
        
        [1,1,2,3,3,0]

        12312
            ^
        for one digit
        we can decode this as 1 and 12, so we have 
        1 and 23 and 12, 12 and 3 and 1 and 2, 
        1 and 2 and 3 and 1 and 2.
        
        for two digit
        we can decode this as as 12 and 3 and 12, 1 and 2 and 
        and 3 and 12, 1 and 23 and 12. we have 6 ways to decode the message
         
        [1,1,2,3,3,6]


        
        
        '''

        dp = [0 for _ in range(len(s) + 1)]

        # base case initialization
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # dp[0]=1 in case we have ""
        dp[0] = 1
        # dp[1] =0 in case we have ''
        dp[1] = 0 if s[0] == "0" else 1  # (1)

        for i in range(2, len(s) + 1):
            # One step jump to check if one single digit is possible to decode it
            # for 123 we have [1,1,0,0]
            # then we decode 1 and we have [1,1,1,0]
            # then we decode 12 and we have [1,1,2,0]
            # then we decode 12 again and we have [1,1,2,2]
            # then we decode 23 and we have [1,1,2,3]
            if 0 < int(s[i - 1:i]) <= 9:  # (2)
                dp[i] += dp[i - 1]
            # Two step jump to check if two digit decode is possible
            if 10 <= int(s[i - 2:i]) <= 26:  # (3)
                dp[i] += dp[i - 2]
        return dp[-1]

def main():
    s = '10'
    solution = Solution()
    res = solution.decode(s)
    print(res)


main()

'''
Time complexity: O(N)
Space complexity: O(1)
'''
