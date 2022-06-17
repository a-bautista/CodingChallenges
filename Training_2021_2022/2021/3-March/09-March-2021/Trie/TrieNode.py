class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26 # length of the English alphabet
        self.isEndOfWord = False
        self.char = char

    def mark_node_as_leaf(self):
        self.isEndOfWord = True
    
    def unmark_node(self):
        self.isEndOfWord = False