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


def removeDuplicates(s, k):
    stack = [['#', 0]]
    for c in s:
        if stack[-1][0] == c:
            # keep adding the count when the c character is equal to the last letter at the top of the stack
            stack[-1][1] += 1
            # remove the elements when the count of the c character is equal to k
            if stack[-1][1] == k:
                stack.pop()
        else:
            # keep adding elements
            stack.append([c, 1])
    return ''.join(c * k for c, k in stack)


def main():
    s = "deeedbbcccbdaa"
    k = 3
    res = removeDuplicates(s,k)
    print(res)



main()

'''
    Time complexity: O(N)
    Space complexity: O(N)
'''