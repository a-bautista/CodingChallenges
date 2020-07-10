from collections import defaultdict

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary(object):
    def __init__(self):
        # initialize the root as a Trie
        self.root = TrieNode()

    def addWord(self, word):
        # initialize the node as the root which is a TrieNode
        node = self.root
        # start adding each letter of the word to the TrieNode
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        # start at the first node
        node = self.root
        # set the result to False
        self.res = False
        # Do DFS to go through all the nodes of the Trie
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        # if the word is "" (empty) which indicates you have reached the
        # end of the Trie
        if not word:
            # if the entire node has a valid word then return True
            if node.isWord:
                self.res = True
            # if the entire node is not a word contained in the Trie then return empty
            return

        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])

        # look for each letter of the word
        else:
            node = node.children.get(word[0])
            # if the node is empty
            if not node:
                return
            # iterate and look if the next letter of the word is contained in the Trie
            self.dfs(node, word[1:])

def main():
    wordDictionary = WordDictionary()
    words= ['dad','daddy','pad','add']
    for word in words:
        wordDictionary.addWord(word)

    # da. will give False because you need a 3 letter word 
    lookFor = ['daddy','mad','da.']
    for word in lookFor:
        res = wordDictionary.search(word)
        print(res)

'''
    Time complexity: Insert is O(k) where k is the length of each char of the word
    Space complexity: O(n*k) 
'''

main()

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)