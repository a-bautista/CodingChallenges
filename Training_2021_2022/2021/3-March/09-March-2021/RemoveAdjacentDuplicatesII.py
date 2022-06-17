'''
    Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them
    causing the left and the right side of the deleted substring to concatenate together.

    We repeatedly make k duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made.

    It is guaranteed that the answer is unique.

    Example 1:

    Input: s = "abcd", k = 2
    Output: "abcd"
    Explanation: There's nothing to delete.

    Example 2:

    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"
    Explanation:
    First delete "eee" and "ccc", get "ddbbbdaa"
    Then delete "bbb", get "dddaa"
    Finally delete "ddd", get "aa"
'''

# manual hashtable
def solve(str1, k):

    stack = [['#', 0]]
    for c in str1:
        # if the last letter is equal to the current letter
        if stack[-1][0] == c:
            # increase the count of the current letter
            stack[-1][-1]+=1
            # in case the current letter has surpassed the limit k then do a pop
            if stack[-1][1] >= k:
                stack.pop()
        # in last letter is not equal to the current letter
        else:
            stack.append([c,1])
     # return the 
    return "".join(c*k for c, k in stack)

def main():
    s = "deeedbbcccbdaa"
    k = 3
    res = solve(s,k)
    print(res)

main()