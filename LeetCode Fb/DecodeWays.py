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


'''

class Solution:
    def decode(self, s):
        if not s:
            return 0

        dp = [0 for _ in range(len(s) + 1)]

        # base case initialization
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1  # (1)

        for i in range(2, len(s) + 1):
            # One step jump
            if 0 < int(s[i - 1:i]) <= 9:  # (2)
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i - 2:i]) <= 26:  # (3)
                dp[i] += dp[i - 2]
        return dp[-1]

def main():
    s = '1111'
    solution = Solution()
    res = solution.decode(s)
    print(res)


main()
