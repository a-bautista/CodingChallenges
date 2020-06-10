from collections import deque

class TreeNode:
    def __init__(self, root):
        self.val = root
        self.left, self.right = None, None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mx = 0
        stack = [[root, root.val, root.val]]
        while len(stack) > 0:
            tmp, cur_mx, cur_mn = stack.pop()
            if tmp.val > cur_mx:
                cur_mx = tmp.val
            if tmp.val < cur_mn:
                cur_mn = tmp.val
            if cur_mx - cur_mn > mx:
                mx = cur_mx - cur_mn
            if tmp.left:
                stack.append([tmp.left, cur_mx, cur_mn])
            if tmp.right:
                stack.append([tmp.right, cur_mx, cur_mn])
        return mx

def main():
    root = TreeNode(3)
    # root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    solution = Solution()
    res = solution.maxAncestorDiff(root)
    print(res)


main()