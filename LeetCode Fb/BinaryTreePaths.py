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
class Node:
    def __init__(self, key):
        self.val = key
        self.left, self.right = None, None

class Solution:
    def solve(self, root):
        def construct_paths(root, current_path):
            if root:
                current_path += str(root.val)
                # if you reach a leaf then append the entire path to the main paths
                if not root.left and not root.right:
                    paths.append(current_path)  # update paths
                else:
                    current_path += '->'  # extend the current path
                    construct_paths(root.left, current_path)
                    construct_paths(root.right, current_path)

        paths = []
        construct_paths(root, '')
        return paths

def main():
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.right = Node(5)
    root = Node(1)
    root.left = Node(4)
    root.right = Node(10)
    root.right.left = Node(2)
    root.left.left = Node(12)
    solution = Solution()
    res = solution.solve(root)
    print(res)



main()

'''
    Time complexity: O(N)
    Space complexity: O(N)
'''