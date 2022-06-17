class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.treeDiameter = 0
    
    def findDiameter(self, root):
        self.helper_find(root)
        return self.treeDiameter

    def helper_find(self, root):

        if root is None:
            return 0

        left = self.helper_find(root.left)
        right = self.helper_find(root.right)

        diameter = left + right + 1
        self.treeDiameter = max(self.treeDiameter, diameter)
        return max(left, right) + 1

def main():
    root  = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right .right = Node(6)
    solution = Solution()
    res = solution.findDiameter(root)
    print(res)

main()