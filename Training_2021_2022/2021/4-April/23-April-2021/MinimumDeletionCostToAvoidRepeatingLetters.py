'''
    Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

    Return the minimum cost of deletions such that there are no two identical letters next to each other.

    Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.    

    Example 1:

    Input: s = "abaac", cost = [1,2,3,4,5]
    Output: 3
    Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).

    Example 2:

    Input: s = "abc", cost = [1,2,3]
    Output: 0
    Explanation: You don't need to delete any character because there are no identical letters next to each other.

    Example 3:

    Input: s = "aabaa", cost = [1,2,3,4,1]
    Output: 2
    Explanation: Delete the first and the last character, getting the string ("aba").

'''

def solve(s, cost):
    maxCost = res = 0
    for i in range(len(s)):
        # if letters are distinct then reset the max cost to 0
        if i > 0 and s[i]!=s[i-1]:
            maxCost = 0
        # sum to res the minimum value from maxCost and the current ith in cost
        res+= min(maxCost, cost[i])
        # get the max cost from the current ith in cost
        maxCost = max(maxCost, cost[i])
    return res

def main():
    s ="abaac"
    cost = [1,2,3,4,5]
    res = solve(s, cost)
    print(res)

main()