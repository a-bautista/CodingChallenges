from TrieNode import TrieNode

class Trie:

    # init
    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        return self.root

    # get the index

    # insert into a Trie
    # time complexity: O(N)
    # space complexity: O(1)
    def insert_into_trie(self, word):

        # edge case
        # 1. No blanks
        if word is None:
            return
        # 2. Invalid values
        

        # define the initial Node
        currentNode = self.root

        # I need to convert the letter into a numeric value
        for c in range(len(word)):
            index =  ord(word[c])-ord('a')

            # insert into the children the letter if it doesn't exist in the current trie
            if currentNode.children[index] is None:
                # convert the new letter into a TrieNode
                currentNode.children[index] = TrieNode(word[c])
                print(word[c]+" has been inserted")
            currentNode = currentNode.children[index]
            

        # indicate that you are done with the Trie
        currentNode.mark_node_as_leaf()
    # seach in a Trie
    # time complexity: O(h) h consecutive levels of a Trie 
    # space complexity: O(1)
    def search(self, word):
        if word is None:
            return 

        # I only want lower case letters
        word = word.lower()

        # set your starting node
        currentNode = self.root
        for char in range(len(word)):
            # convert each letter to an index
            index = ord(word[char])-ord('a')

            # the node for a letter doesn't exist
            if currentNode.children[index] is None:
                return False

            # go onto the next node based on the index
            currentNode = currentNode.children[index]

        # we foiund each node inside a letter and the last node has end of word as true            
        if currentNode is not None and currentNode.isEndOfWord:
            return True

        return False


    # delete a Trie
    # We have 3 cases
    # 1. The word exists and there's not any suffix or prefix --> go over each node recursively
    # 2. The word exists and there's a prefix --> go over each node and mark the last node as False
    # 3. The word has a common prefix --> If the word to be deleted has a common prefix and the last node 
    #    of that word does not have any children, then this node is deleted along with all the parent nodes

    def delete(self, word):
        if self.root is None or word is None:
            print("No key or empty trie error")
            return 
        self.delete_helper(key, self.root, len(key), 0)
        
    # recursive function to delete nodes
    def delete_helper(self, key, current_node, length, level):
        deleted_self = False



    def get_words(self, root, result, level, word):
        if root.isEndOfWord:
            temp = ""
            for x in range(level):
                temp+=word[x]
            result.append(str(temp))

        # we start a - z (0 - 25)
        for i in range(26):
            # if we find a children at letter i(0,...26) then we add this node and continue traversing the Trie
            # and we go in an alphabetical order
            if root.children[i]:
                # convert the inserted key of the Trie into the corresponding letter
                # Non-None child, so add that index to the character array
                word[level] = chr(i + ord('a'))  # Add character for the level
                # we go to the children of each node to get each word recursively, i.e.,
                # root
                #  |  \
                #  a   c
                #  |   |
                #  s   a
                #      |
                #      r
                # you start with letter a then you go down one level to a and we are going
                # in alphabetical order 0 - 26 or a - z
                self.get_words(root.children[i], result, level+1, word)

    # find all words in a Trie
    def find_words(self, root):
        # store all the results in this list
        result = []
        # we are assuming the max length of a word is 30, so we create an array of 30 Nones and the max
        # depth level is 30
        word = [None]*30 
        self.get_words(root, result, 0, word)
        return result

    def sort_list(self, nums):
        # you insert the words in a trie and then you return the results from the list retrieved in alphabetical order
        result = []
        trie = Trie()
        for x in range(len(nums)):
            self.insert_into_trie(nums[x])

        # you retrieve the words from the Trie in alphabetical order
        word = ['']*30
        self.get_words(self.get_root(), result, 0, word)
        return result

def main():
    words = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]

    words2 = ["as", "car", "arm"]

    output = ["Not present", "Present"]

    t = Trie()
    t2 = Trie()
    print(t2.sort_list(words))

    for i in range(len(words2)):
        t.insert_into_trie(words2[i])

    # Search for different keys
    if t.search("the") is True:
        print("the --- " + output[1])
    else:
        print("the --- " + output[0])

    if t.search("these") is True:
        print("these --- " + output[1])
    else:
        print("these --- " + output[0])

    # find words
    res = t.find_words(t.root)
    print(res)

main()
    