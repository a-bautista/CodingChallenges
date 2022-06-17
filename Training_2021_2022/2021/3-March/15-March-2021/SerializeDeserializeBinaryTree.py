class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root):
        return self.helper_serialize(root, [])

    def helper_serialize(self, root, serializedList):
        if root is None:
            serializedList.append("None")
        else:
            # append each node in a pre order fashion (root-left-right)
            serializedList.append(str(root.val))
            self.helper_serialize(root.left, serializedList)
            self.helper_serialize(root.right, serializedList)
        return serializedList

    def deserialize(self, deserializedList):
        root = self.helper_serialize(deserializedList)
        return root

    def helper_deserialize(self, nodeList):

        if nodeList[0] == None:
            nodeList.pop(0)
            return None

        root = Node(nodeList.pop(0))
        root.left = self.helper_deserialize(nodeList)
        root.right = self.helper_deserialize(nodeList)
        return root

def main():

    tree = Node(4)
    tree.left = Node(3)
    tree.right = Node(8)
    tree.left.left = Node(1)
    tree.left.left.right = Node(2)

    serializedTree = Solution()
    serializedTreeList = serializedTree.serialize(tree)
    print(serializedTreeList)

    deserializedTree = Solution()
    deserializedTreeNodes = deserializedTree.deserialize(serializedTreeList)
    deserializedTree.print_preorder(deserializedTreeNodes)
    #print(deserializedTreeNodes.print_preorder)

main()
