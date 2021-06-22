from collections import defaultdict
class Solution:
    def numSimilarGroups(self, A):

        adj = defaultdict(set)
        set_A = set(A)
        if len(A) < len(A[0]):
            for i in range(len(A)):
                for j in range(i + 1, len(A)):
                    word1 = A[i]
                    word2 = A[j]
                    count = 0
                    for j, k in zip(word1, word2):
                        if j != k:
                            count += 1
                    if count == 2:
                        adj[word1].add(word2)
                        adj[word2].add(word1)
        else:
            for word in A:
                temp = list(word)
                for i in range(len(word)):
                    for j in range(i + 1, len(word)):
                        temp[i], temp[j] = temp[j], temp[i]
                        temp_b = "".join(temp)
                        if temp_b in set_A:
                            adj[word].add(temp_b)
                            adj[temp_b].add(word)
                        temp[i], temp[j] = temp[j], temp[i]

        components = 0
        visited = set()

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for child in adj[node]:
                    dfs(child)

        for word in A:
            if word not in visited:
                components += 1
                dfs(word)
        return components

'''
    Time complexity:  O(N(L^2))
'''