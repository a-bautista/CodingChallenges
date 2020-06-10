from typing import List

def main():
    myProducts1 = ["mobile","mouse","moneypot","monitor","mousepad"]
    keyword1    = "mouse"
    myProducts2 = ["bags","baggage","banner","box","cloths"]
    keyword2    = "bags"
    myProducts3 = ["havana"]
    keyword3 = "havana"
    keyword4 = "tatiana"

    solution = Solution.suggestedProducts(Solution, myProducts3, keyword4)
    print(solution)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        if not products or not searchWord:
            return []
        trie = Trie()
        for word in products:
            trie.insert(word)
        return trie.find(searchWord)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.words.append(word)

    def find(self, word):
        ret = []
        curr = self.root
        for char in word:
            if char not in curr.children:
                break
            curr = curr.children[char]
            ret.append(sorted(curr.words)[:3])

        for i in range(len(word) - len(ret)):
            ret.append([])
        return ret

if '__main__' == __name__:
    main()

'''Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. '''

'''
    Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
    Output: [
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
    ]
    Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
    After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
    After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

    Input: products = ["havana"], searchWord = "havana"
    Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

    Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
    Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

    Input: products = ["havana"], searchWord = "tatiana"
    Output: [[],[],[],[],[],[],[]]

'''