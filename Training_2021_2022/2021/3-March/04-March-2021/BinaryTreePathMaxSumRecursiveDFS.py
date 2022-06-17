class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def solve_dfs_recursive(root):
    max_sum = float('-inf')
    def recursion_call(node):
        nonlocal max_sum
        leftPath = 0
        rightPath = 0

        # base case
        if not node: return 0

        # traverse the tree in DFS to reach the left node and then assign the value of the left path
        if recursion_call(node.left) >0:
            leftPath = recursion_call(node.left)

        # traverse the tree in DFS to reach the right node and then assign the value of the right path
        if recursion_call(node.right)>0:
            rightPath = recursion_call(node.right)

        # construct the newPath and then check if this is greater than the existing one in the max_sum
        priceNewPath = node.val + leftPath + rightPath
        max_sum = max(max_sum, priceNewPath)

        # for recursion :
        # return the max contribution if continue the same path
        return node.val + max(leftPath, rightPath)

    recursion_call(root)
    return max_sum

# def maxPathSum(root):
#     max_sum = float('-inf')
#
#     def max_contrib(node):
#         nonlocal max_sum
#         left_subtree, right_subtree = 0, 0
#
#         if not node: return 0
#
#         # max sum on the left and right sub-trees of node
#         if max_contrib(node.left) > 0:
#             left_subtree = max_contrib(node.left)
#         if max_contrib(node.right) > 0:
#             right_subtree = max_contrib(node.right)
#
#         # the price to start a new path where `node` is a highest node
#         price_newpath = node.val + left_subtree + right_subtree
#
#         # update max_sum if it's better to start a new path
#         max_sum = max(max_sum, price_newpath)
#
#         # for recursion :
#         # return the max contribution if continue the same path
#         return node.val + max(left_subtree, right_subtree)
#
#     max_contrib(root)
#     return max_sum



def main():
    root = TreeNode(-8)
    root.left = TreeNode(2)
    root.right = TreeNode(17)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(19)
    root.right.right = TreeNode(5)
    print(solve_dfs_recursive(root))

main()