'''

    Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
    Answers within 10-5 of the actual answer will be accepted.

         3
        / \
       9  20
          / \
         15  7

    Input: root = [3,9,20,null,null,15,7]
    Output: [3.00000,14.50000,11.00000]

    Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
    Hence return [3, 14.5, 11].

'''

from collections import deque
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def solve(root):
    queue = deque()
    queue.append(root)
    res = []

    while queue:
        temp = []
        size = len(queue)

        for _ in range(size):
            current_node = queue.popleft()
            temp.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        # finished adding the values
        res.append(sum(temp)/size)

    return res

def main():

    node       = Node(3)
    node.left  = Node(9)
    node.right = Node(20)
    node.right.left  = Node(15)
    node.right.right = Node(7)

    solution = solve(node)
    print(solution)

main()

