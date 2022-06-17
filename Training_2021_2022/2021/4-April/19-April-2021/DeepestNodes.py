'''
    Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

    A node is deepest if it has the largest depth possible among any node in the entire tree.

    The subtree of a node is that node, plus the set of all descendants of that node.

    Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

    Example 1:

    Input: [3,5,1,6,2,0,8,null,null,7,4]
    Output: [2,7,4]
    Explanation:

         3
        /  \
       5    1
      / \   /\
     6   2 0   8   
         /\
        7  4

    BFS+LCA combo     
'''


from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# O(N)
def lca(root, p, q):
    if not root:
        return None
    if root.val in (p.val, q.val):
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left or right


def bfs(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        size = len(queue)
        temp = []
        for _ in range(size):
            currentNode = queue.popleft()
            if currentNode:
                temp.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        # only get the last subtree from the deepest level, the subtree should be either a pair or just a single value
        if len(temp)>2:
            temp.pop()
        res.append(temp)
    return res[-1]

    # delete the all the nodes [:-1] the last pair are the last nodes

def main():
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    #root.left.right.left = Node(7)
    #root.left.right.right = Node(4)
    root.right = Node(1)
    root.right.left = Node(0)
    root.right.right = Node(8)
    root.right.right.right = Node(10)
    #root.right.right.right.right = Node(11)

    res = bfs(root)
    sol = None
    if len(res)>=2:
        p = Node(res[0])
        q = Node(res[1])
        sol = lca(root, p, q)
    elif len(res)==1:
        p = q = Node(res[0])
        sol = lca(root, p, q)
    print(res)
    print(sol.val)
    #print(res)

main()