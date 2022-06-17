'''
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a 
    binary tree and inorder is the inorder traversal of the same tree, construct and return 
    the binary tree.

         3
        / \
       9   20
          /  \
         15   7

    Input: 
        preorder = [3,9,20,15,7], 
        inorder = [9,3,15,20,7]
    Output: 
        [3,9,20,null,null,15,7] 
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# recursive solution
def solve(preorder, inorder):
    
    #if preorder[0]==-1 or inorder[0]==-1:
    #    return -1
    if inorder:
        # avoid modifying the lists because they can cause you trouble later
        # middle = preorder.pop(0)
        middle = inorder.index(preorder.pop(0))
        root = Node(inorder[middle])
        left_subtree = solve(preorder, inorder[:middle])
        right_subtree = solve(preorder, inorder[middle+1:])
        return root

# solution O(N)
def solve_hashmap(preorder, inorder):
    hashmap_inorder_index = {}
    def rec(left, right):
        
        nonlocal preorderIndex 
        if left < right:
            return None

        rootValue = preorder.index(preorderIndex)
        root = TreeNode(rootValue)
        preorderIndex +=1

        root.left = rec(left, hashmap_inorder_index[rootValue] - 1)
        root.right = rec(hashmap_inorder_index[rootValue]+1, right)

        return root

    preorderIndex = 0
    for index, value in enumerate(inorder):
        hashmap_inorder_index[value] = index

    return rec(0, len(inorder) - 1)


def main():
    preorder = [3,9,20,15,7] 
    inorder = [9,3,15,20,7]
    res = solve(preorder, inorder)
    print(res)

main()