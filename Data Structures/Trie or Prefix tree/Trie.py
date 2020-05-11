'''

    Inserting a node in a Trie:
        Every character of input key is inserted as an individual trie node, i.e.,

            N = number of keys (Tree and Trie = 2 words)
            k = is the length of the keys (Tree = 4 characters and Trie = 4 characters)

            Trie and Tree represented

            root
             |
            'T'
             |
            'r'     for node r, we have 2 children
             |  \
            'i' 'e'
             |   \
            'e'  'e' -> leaf nodes

        If the input key is new or an extension of existing key, we need to construct non-existing nodes of the key, and
        mark leaf node.

        The children is an array of pointers to next level trie nodes.

        Time complexity:
            insert 	O(k) where k is the length of the key.
            lookup 	O(k)

        Space complexity:
            N = number of keys (Tree and Trie = 2 words)
            k = is the length of the keys (Tree = 4 characters and Trie = 4 characters)
            O(n∗k)



'''


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any","by", "their"]
    output = ["Not present in trie","Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie for every key
    for key in keys:
        t.insert(key)


class TrieNode:
    def __init__(self):
        self.children = [None] * 26

        # isEnd returns True if it is the end of the word
        self.isEnd = False


class Trie():
    def __init__(self):
        self.root = self.getNode() # call getNode to create a TrieNode

    def getNode(self):

        # returns a new Trie node (initialized to NULLs)
        return TrieNode()


    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        return ord(ch)-ord('a')



    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        crawl = self.root # create an initial Trie node with 26 characters
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level]) # convert each character of the key into an indexed value

            # if the character of the new key is not found in the existing Trie, then create a new Trie with 26 characters as done before
            if not crawl.children[index]:
                crawl.children[index] = self.getNode()

            crawl = crawl.children[index] # move onto the next node of the Trie and insert the new index


        crawl.isEnd = True # mark the end of the key with True


    def search(self, key):

        crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not crawl.children[index]:
                return False
            crawl = crawl.children[index]

        return crawl != None and crawl.isEnd

if __name__ == '__main__':
    main()










    def __contains__(self, item):
        pass

    def node(self, char):
        return self[char - 'a']

    def setEnd(self):
        self._isEnd = True

    def isEnd(self):
        return self.isEnd
