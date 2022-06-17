'''
        1
      /  \
     4   10
        /  \
       2    12

    1->4
    1->10->2
    1->10->12

'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def solve(self, root):
        def dfs_recursive(root, current_path):

            if root:   
                #self.res.append([str(self.root.val)+"->"])
                current_path += str(root.val)
                if not root.left and not root.right:
                    paths.append(current_path)
                else: 
                    current_path+="->"
                    dfs_recursive(root.left, current_path)
                    dfs_recursive(root.right, current_path)

        paths = []
        dfs_recursive(root, '')
        return paths

def main():
    root = Node(1)
    root.left = Node(4)
    root.right = Node(10)
    root.right.left = Node(2)
    root.right.right = Node(12)
    solution = Solution()
    res = solution.solve(root)
    #res = dfs_recursive(root)
    print(res)

main()