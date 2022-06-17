'''
    Given a binary tree where each node can only have a digit (0-9) value, 
    each root-to-leaf path will represent a number. Find the total sum of all 
    the numbers represented by all paths.

         1
        / \
       7    9
           / \
          2   9

    17 + 192 + 199 = 408
'''

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution:
    def solve(self, root):
        allPaths = []
        self.backtrack(root, [], allPaths)
        return sum(allPaths)

    def backtrack(self, root, currentPath, allPaths):

        if not root:
            return

        # append the current root to the path
        currentPath.append(str(root.val))

        # the node has no children
        if root.left is None and root.right is None:
            temp = list(map(int, currentPath))
            allPaths.append(sum(temp))

        else:
            self.backtrack(root.left, currentPath, allPaths)
            self.backtrack(root.right, currentPath, allPaths)

        # backtrack, delete the last inserted value
        del currentPath[-1]

def main():
    root = Node(12)
    root.left = Node(7)
    root.right = Node(1)
    root.left.left = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(5)
    solution = Solution()
    res = solution.solve(root)
    #print(res)
    print("Sum of Path numbers: " 
           + str(solution.solve(root)))


main()
