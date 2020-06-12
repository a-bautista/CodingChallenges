"""
    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

    Example:

    You may serialize the following tree:

        1
       / \
      2   3
         / \
        4   5

    as "[1,2,3,null,null,4,5]"


    Time complexity : in both serialization and deserialization functions, we visit each node exactly once,
    thus the time complexity is O(N), where NNN is the number of nodes, i.e. the size of tree.

    Space complexity : in both serialization and deserialization functions, we keep the entire tree, either at the
    beginning or at the end, therefore, the space complexity is O(N).

"""

# Serialization: Converting a tree into a list

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """
        Encode a tree into a list of strings.
        :param root: TreeNode
        :return: []
        """
        return self.helper_rserialize(root,[])

    def helper_rserialize(self, root, rserialized):
        if root is None:
            rserialized.append('None')
        else:
            # pre-order (root-left-right)
            rserialized.append(str(root.val))
            rserialized = self.helper_rserialize(root.left, rserialized)
            rserialized = self.helper_rserialize(root.right, rserialized)
        return rserialized

    def dserialize(self, rserialized_list):

        #node_list = rserialized_list.split(",")
        root = self.helper_deserialize(rserialized_list)
        return root

    def helper_deserialize(self, node_list):

        if node_list[0] == 'None':
            node_list.pop(0)
            return None

        root = TreeNode(node_list[0])
        node_list.pop(0)
        root.left = self.helper_deserialize(node_list)
        root.right = self.helper_deserialize(node_list)
        return root

    def print_preorder(self, root):

        if root:
            print(root.val)
            self.print_preorder(root.left)
            self.print_preorder(root.right)

def main():

    tree = TreeNode(4)
    tree.left = TreeNode(3)
    tree.right = TreeNode(8)
    tree.left.left = TreeNode(1)
    tree.left.left.right = TreeNode(2)

    serializedTree = Codec()
    serializedTreeList = serializedTree.serialize(tree)
    print(serializedTreeList)

    deserializedTree = Codec()
    deserializedTreeNodes = deserializedTree.dserialize(serializedTreeList)
    deserializedTree.print_preorder(deserializedTreeNodes)
    #print(deserializedTreeNodes.print_preorder)

main()


"""
    Time complexity: O(N)where n is the number of nodes
    Space complexity: O(N)
"""