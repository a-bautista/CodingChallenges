"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

    1. Push all the left nodes into a stack when you initialize the BSTIterator.
    2. The stack will always keep the lowest value because we inserted all the left child nodes.
    3. When you call next, you pop the lowest value and then you insert the right value. 
    
      6
    4  10
   2 5 8 12

   2      
   4   -> 4  -> 5  ->   ->    ->  8 ->     ->    -> done
   6      6     6     6    10    10    10     12
   
   The number 2 doesn't have any child, so just pop it.
   
   The number 4 has a child (5), so pop 4 and then insert the child 5. 
   
   The number 5 doesn't have children, so pop the value.
   The number 10 has 2 children, so insert 10 then you insert 8.
   The number 8 doesn't have children, so pop the value.
   The number 10 has a right child, so pop the value and insert 12. 
   
   You need to define the attribute values: a stack and the pushAll elements.
   You need to define the 3 methods, hasNext, next and pushAll.
   
"""

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = list()
        self.pushAll(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    # return an integer, the first element in the stack (lowest number) and push the right nodes
    def next(self):
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val

    # push all the left nodes into the stack
    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left


def main():
    obj = BSTIterator(7)
    param_1 = obj.next()
# param_2 = obj.hasNext()

main()
"""

Time complexity: O(N) where n is the number of nodes. 
Space complexity: O(N)

"""