'''

    Given a binary tree, return all root-to-leaf paths.

    Note: A leaf is a node with no children.

    Example:

    Input:

    1
  /   \
 2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3


'''

class Solution:
    def __init__(self):
        self.paths = []

    def construct_paths(self, root, current_path):

        if root:
            current_path += str(root.val)
            # if you reach a leaf then append the entire path to the main paths
            if not root.left and not root.right:
                self.paths.append(current_path)  # update paths
            else:
                current_path += '->'  # extend the current path
                self.construct_paths(root.left, current_path)
                self.construct_paths(root.right, current_path)

        #paths = []
        self.construct_paths(root, '')
        return self.paths

'''
    Time complexity: O(N)
    Space complexity: O(N)

'''