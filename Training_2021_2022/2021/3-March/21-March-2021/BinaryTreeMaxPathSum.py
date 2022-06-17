# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def __init__(self):
    #     self.maxSum = float('-inf')
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.rec_max_path(root)
        return self.res
        
    def rec_max_path(self, root):
        
        if not root:
            return 0
        
        left = max(self.rec_max_path(root.left),0)
        right = max(self.rec_max_path(root.right),0)
        
        priceNewPath = root.val + left + right
        
        self.res = max(priceNewPath, self.res)
        
        return root.val + max(left, right)

def main():
    root = TreeNode(-8)
    root.left = TreeNode(2)
    root.right = TreeNode(17)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(19)
    root.right.right = TreeNode(5)
    solution = Solution()
    res = solution.maxPathSum(root)
    print(res)

main()