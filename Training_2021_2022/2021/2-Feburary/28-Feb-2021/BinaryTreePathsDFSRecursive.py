class Node:
    def __init__(self, key):
        self.val = key
        self.left, self.right = None, None

class Solution:
    def solve(self, root):

        def recursion(root, current_path):
            if root:
                # get the current value of root
                current_path += str(root.val)
                # if you have reached a leaf node then you have reached the end of the tree path, so add the entire path
                if not root.left and not root.right:
                    paths.append(current_path)
                # if you haven't reached the leaf node then you need to continue traversing the tree
                else:
                    current_path += '->'
                    recursion(root.left, current_path)
                    recursion(root.right, current_path)

        paths = []
        recursion(root, '')
        return paths

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(5)
    solution = Solution()

    res = solution.solve(root)
    print(res)
    # root = Node(1)
    # root.left = Node(4)
    # root.right = Node(10)
    # root.right.left = Node(2)
    # root.left.left = Node(12)
    # solution = Solution()
    # res = solution.solve(root)
    # #res = solve_dfs_paths(root)
    # print(res)

main()

'''
    Time complexity: O(N)
    Space complexity: O(N)
'''