'''

    Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

    For example:
    Given binary tree [3,9,20,null,null,15,7],

       3
      / \
     9  20
       /  \
      15   7


    Following the description of the problem, the most intuitive solution would be the BFS (Breadth-First Search)
    approach through which we traverse the tree level-by-level.
    The default ordering of BFS within a single level is from left to right. As a result, we should adjust the
    BFS algorithm a bit to generate the desired zigzag ordering.


'''

from collections import deque

class TreeNode:
    def __init__(self,key):
        self.right = None
        self.left  = None
        self.val   = key


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        left = True
        result = deque()
        tmp = deque([(root, 0)])
        while tmp:
            node, depth = tmp.popleft()
            if node:
                if len(result) <= depth:
                    result.append(deque())
                    left = (not left)
                if left:
                    result[depth].appendleft(node.val)
                if not left:
                    result[depth].append(node.val)
                if node.left:
                    tmp.append((node.left, depth + 1))
                if node.right:
                    tmp.append((node.right, depth + 1))
        return result

def main():

    Tree = TreeNode(3)
    Tree.right = TreeNode(9)
    Tree.left = TreeNode(20)
    Tree.left.left = TreeNode(15)
    Tree.left.right = TreeNode(28)
    solution = Solution()
    res = solution.zigzagLevelOrder(Tree)
    print(res)

main()