"""
    Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is
    the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

          1
         / \
        2   3
        |  / \
        4 5   6

    Return 5, which is the length of the path [4,2,1,3,6] or [4,2,1,3,5].

          1
         / \
        2   3
           / \
          5   6
        / |   |
       7  8   9
          |   |
          10  11

    Return 7 which is the length of the path [10, 8, 5, 3, 6, 9, 11].

    Remember the diameter is the longest distance between any 2 nodes and the root might not be considered
    part of the path.

    [2,1,3,5,7]
    [2,1,3,5,8,10]
    [2,1,3,6,9,11]
    [7,5,3,6,9,11]
    [10,8,5,3,6,9,11] result

    We can use DFS to go down into each node and then we determine the max value between the answer and the sum of L+R+1 (+1
    in case you have reached lowest node).

    Algorithm:
        1. We need to calculate the height of both the children and the parent node.
        2. We can use two recursive calls similar to DFS.
        3. The height of the current node will be equal to the sum path of the left and
            the right node plus 1 (to include the parent node).
        4.

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        self.diameterOfBinaryTree(root)
        return self.treeDiameter

    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        L = self.diameterOfBinaryTree(root.left)
        R = self.diameterOfBinaryTree(root.right)

        diameter = L + R + 1

        self.treeDiameter = max(self.treeDiameter, diameter)
        return max(L, R) + 1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()