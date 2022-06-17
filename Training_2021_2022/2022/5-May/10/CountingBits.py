'''
    Given an integer n, return an array ans of length n + 1 such that for each i 
    (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

    Example 1:

    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    Example 2:

    Input: n = 5
    Output: [0,1,1,2,1,2] 
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101

    There are 2 ones when we reach 5.

    The logic behind this problem:

    Even values = dp[current_value // 2]
    Odd values = dp[current_value -1] + 1= result of the previous value + 1

    Index: 0 1 2 3 4 5 6 7
    Res:   0 1 1 2 1 2 2 3

         dp[0] = 0
    odd  dp[1] = 1
    even dp[2] = dp[2 // 2] = 1 # look at dp[1], that's the answer
    odd  dp[3] = dp[3 - 1] + 1 = 2
    even dp[4] = dp[4 // 2] = 1 # look at dp[2], that's the answer
    odd  dp[5] = dp[5 - 1] + 1= 2
    even dp[6] = dp[6//2] = 2 # look at dp[3], thats' the answer


'''

def sol(num):
    dp = [0]
    for i in range(1, num+1):
        # computing odd values
        if i % 2 == 1:
            dp.append(dp[i - 1] + 1)
        # computing even values
        else:
            dp.append(dp[i // 2])
    return dp

def main():
    res = sol(10)
    print(res)
    
main()