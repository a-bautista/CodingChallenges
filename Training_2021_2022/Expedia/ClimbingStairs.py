'''
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Example 1:

        Input: n = 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

    Example 2:

        Input: n = 3
        Output: 3
        Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step


    This is fibonacci sequence because:

        stairs:  0 | 1 | 2 | 3 | 4 | 5
        ways:    0 | 1 | 2 | 3 | 5 | 8
        
        # of ways to climb: 

                1 stair: 1 way
                    1

                2 stairs: 2 ways
                    1 + 1
                    2

                3 stairs: 3 ways
                    1 + 1 + 1
                    2 + 1
                    1 + 2

                4 stairs: 
                    1 + 1 + 1 + 1
                    2 + 2
                    2 + 1 + 1
                    1 + 2 + 1
                    1 + 1 + 2

    Time complexity: O(N)
    Space complexity: O(N)
'''

def climb_recursive(n):
    if n==1:
        return 1
    
    if n == 2:
        return 2
    
    return climb_recursive(n-1) + climb_recursive(n-2)

class SolutionMemoization:
    memo = dict()
    memo[1] = 1
    memo[2] = 2

    def climb_memoization(self, n):
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climb_memoization(n-1) + self.climb_memoization(n-2)
            return self.memo[n]
    
        
def climb_dp(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # considering 0 steps we need n + 1 places
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
    

def main():

    stairs = 5
    sol_recursive = climb_recursive(stairs)
    # print(sol_recursive)

    solution_memoization = SolutionMemoization()
    sol = solution_memoization.climb_memoization(stairs)
    print(sol)

    solution_dp = climb_dp(stairs)
    print(solution_dp)

main()