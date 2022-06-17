'''
    Given the root of a binary tree and an array of TreeNode objects nodes, 
    return the lowest common ancestor (LCA) of all the nodes in nodes. 
    All the nodes will exist in the tree, and all values of the tree's nodes are unique.

             3
            / \
           5   1 
          / \  / \
         6   2 0  8 
            / \
           7   4

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
    Output: 5
    Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.            
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.lca = None

class Solution:
    def lowestCommonAncestor(self, root, nodes):
        nodes = set(nodes)
        
        def recu_LCA(root):
            if not root:
                return None
            if root.val in nodes:
                return root
            
            left, right = recu_LCA(root.left), recu_LCA(root.right)
            if left and right:
                return root
            # either branch should contain the root value 
            return left or right    
        return recu_LCA(root)

    # nodes = set(values)
    # def recu(root):
    #     if not root:
    #         return None
    #     if root in nodes:
    #         return root
    #     left = recu(root.left)
    #     right = recu(root.right)

    #     if left and right:
    #         return root
    #     return left or right

    return recu(root)

def main():
    tree = TreeNode(3)
    tree.left = TreeNode(5)
    tree.right = TreeNode(1)
    tree.left.left = TreeNode(6)
    tree.left.right = TreeNode(2)
    tree.right.left = TreeNode(0)
    tree.right.right = TreeNode(8)
    tree.left.right.left = TreeNode(7)
    tree.left.right.right = TreeNode(4)
    solution_lca = Solution()
    lca = solution_lca.lowestCommonAncestor(tree, [2, 0, 8])

    #result = tree.lowestCommonAncestor(tree,TreeNode(4), TreeNode(5))
    print("The LCA is : " + str(lca.val))

main()