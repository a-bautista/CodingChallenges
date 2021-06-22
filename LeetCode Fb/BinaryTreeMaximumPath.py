"""
    Path with Maximum Sum (hard) #

    Find the path with the maximum sum in a given binary tree.
    Write a function that returns the maximum sum.
    A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily
    pass through the root.


    Binary Tree Maximum Path Sum
     -10
    /   \
   9     20
        /  \
      15    7


    We need to get the max values of the child nodes but this is through the roots, and these are excluded.

    We need to get the max sum in a path of the tree.

        max_sum = - inf
        -10
            Bring the left and right children of 10
            9 , [20,15,7]
            bring the left and right children of 9
            0, 0
            path = Add the sum of 9 + right child + left child
            Compare the path with the defined max_sum
            max_sum = max(max_sum, path) # 9
            return 9 + max(0,0) to node 10

            Bring the left and right children of 20
            15, 7
                Bring the children of 15
                0,0
                path = Add the sum of 15 + right child + left child
                Compare the new path with the max_sum
                max_sum = max_sum(max_sum, path) # 9<15, assign 15
                return 15 + max(0,0) to the node 20

                Bring the left and right children of 7
                0,0
                path = Add the sum of 7 + 0+ 0
                max_sum = max_sum(max_sum, path) # still 15
                return 7 + max(0, 0) to node 20

            path = 15 + 7 + 20 (left child +right child of 20)
                 = 42

            max_sum = max(42, 15) # 42 is the new value
            return  node.val + max(right child, left child) # 20 + max(15,7) to node -10

            path = -10 + right child + left child
                 = -10 + 35 + 9
                =  34

            max_sum = max(34, 42) # still 42
            return node.val + max(right gain, left_gain) # -10 + 35 = 25
        return max

"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


# class Solution:
#     def maxPathSum(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         def max_gain(node):
#             nonlocal max_sum
#             if not node:
#                 return 0
#
#             # max sum on the left and right sub-trees of node, use the max to restrict this to only positive values
#             left_gain = max(max_gain(node.left), 0)
#             right_gain = max(max_gain(node.right), 0)
#
#             # the price to start a new path where `node` is a highest node
#             price_newpath = node.val + left_gain + right_gain
#
#             # update max_sum if it's better to start a new path
#             max_sum = max(max_sum, price_newpath)
#
#             # maximum sum of any path from the current node will be equal to the maximum of
#             # the sums from left or right subtrees plus the value of the current node
#             return node.val + max(left_gain, right_gain)
#
#         max_sum = float('-inf')
#         max_gain(root)
#         return max_sum

class Solution:

    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_gain(root)
        return self.max_sum

    def max_gain(self,node):
        #nonlocal max_sum
        if not node:
            return 0

        # max sum on the left and right sub-trees of node, use the max to restrict this to only positive values
        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)

        # the price to start a new path where `node` is a highest node
        price_newpath = node.val + left_gain + right_gain

        # update max_sum if it's better to start a new path
        self.max_sum = max(self.max_sum, price_newpath)

        # maximum sum of any path from the current node will be equal to the maximum of
        # the sums from left or right subtrees plus the value of the current node
        return node.val + max(left_gain, right_gain)


def main():

    tree             = TreeNode(12)
    tree.left        = TreeNode(7)
    tree.right       = TreeNode(1)
    tree.left.left   = TreeNode(9)
    tree.right.left  = TreeNode(10)
    tree.right.right = TreeNode(5)

    solution = Solution()
    res = solution.maxPathSum(tree)
    print(res)

main()


"""
    Time complexity: O(N)
    Space complexity: O(1)
"""