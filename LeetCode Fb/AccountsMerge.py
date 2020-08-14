'''

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email
that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people
as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely
have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name,
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:

Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"],
["Mary", "mary@mail.com"]]

Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

'''

from collections import defaultdict
class Solution(object):
    def accountsMerge(self, accounts):
        # Build up the graph such as the following:
        # cache = { 'johnsmith@mail.com': [0,1]
        #           'john_newyork@mail.com':[1],
        #           'mary@mail.com': [2],
        #           'johnnybravo@mail.com': [3]
        #          }

        res = []
        # this is used to indicate which elements of the list or nodes have been visited
        visited = set()
        cache = defaultdict(list)
        for i, account in enumerate(accounts):
            # I start in 1 because I want the emails and position 0 is the name
            for email in account[1:]:
                cache[email].append(i)

        # dfs code for traversing the graph and add results
        def dfs(idx,sub_res):
            if idx in visited:
                return
            # add the visited node to the current set
            visited.add(idx)
            for email in accounts[idx][1:]:
                sub_res.add(email)
                # I am traversing each node of the accounts list, because for john I want to get the following structure
                # {'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'}

                # The first element (john00@mail.com) is the last time where the johnsmith@mail value appeared in:
                # 0 ['John', 'johnsmith@mail.com', 'john_newyork@mail.com'],
                # 1 ['John', 'johnsmith@mail.com', 'john00@mail.com'],
                for records in cache[email]:
                    dfs(records, sub_res)

        for idx, account in enumerate(accounts):
            # tmp_res contains the values of the traversed nodes
            tmp_res = set()
            dfs(idx, tmp_res)
            if tmp_res:
                # return the name of the account and the traversed nodes
                res.append([account[0]] + sorted(list(tmp_res)))
        return res


def main():
    # accounts = [
    #             ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    #             ["John", "johnsmith@mail.com", "john00@mail.com"],
    #             ["John", "johnnybravo@mail.com"],
    #             ["Mary", "mary@mail.com"]
    #             ]
    accounts = [
        ["John", "john00@mail.com"],
        ["John", "john00@mail.com", "johnbravo@mail.com"],
        ["Mary", "mary@mail.com", "mary@mail.com"]
    ]

    solution = Solution()
    res = solution.accountsMerge(accounts)
    print(res)


main()

'''
    Time complexity: O(Sigma(a*log(a))) where a is the length of accounts.
    Space complexity: O(Sigma(a)) which is the space used in the graph.
'''

