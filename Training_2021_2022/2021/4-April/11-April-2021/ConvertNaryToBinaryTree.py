'''
N-ary tree
     1
   / | \
  2  3  4
    / \
   5   6

Must be converted to binary tree

    1
     \
      2
       \
        3
       / \
      5   4
     /
    6 
'''
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None

        rootNode = TreeNode(root.val)
        queue = deque([(rootNode, root)])

        while queue:
            parent, curr = queue.popleft()
            prevBNode = None
            headBNode = None
            # traverse each child one by one
            for child in curr.children:
                newBNode = TreeNode(child.val)
                if prevBNode:
                    prevBNode.right = newBNode
                else:
                    headBNode = newBNode
                prevBNode = newBNode
                queue.append((newBNode, child))

            # use the first child in the left node of parent
            parent.left = headBNode

        return rootNode
        
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        """Decodes your binary tree to an n-ary tree.
        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None

        # should set the default value to [] rather than None,
        # otherwise it wont pass the test cases.
        rootNode = Node(data.val, [])

        queue = deque([(rootNode, data)])

        while queue:
            parent, curr = queue.popleft()

            firstChild = curr.left
            sibling = firstChild

            while sibling:
                # Note: the initial value of the children list should not be None, which is assumed by the online judge.
                newNode = Node(sibling.val, [])
                parent.children.append(newNode)
                queue.append((newNode, sibling))
                sibling = sibling.right

        return rootNode
        

def main():

    node1 = Node(1, Node(2))
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    # append the children of the node 1
    node1.children(node2)
    node1.children(node3)
    node1.children(node4)

    node5 = Node(5)
    node6 = Node(6)

    # append the children of the node 3
    node3.children(node5)
    node3.children(node6)

    solution = Solution()
    solution.convert_n_ary_to_bt(node1)

main()
    
'''
    Time complexity: O(N)
    Space complexity: O(L)
'''