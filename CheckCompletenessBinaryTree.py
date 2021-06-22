from collections import deque
class Solution:
    def solve(self, root):
        if root is None:
            return True

        queue = deque()
        queue.append(root)
        isNullAbove = False
        while queue:
            currentLevel = len(queue)
            isNull = False
            for _ in range(currentLevel):
                currentNode = queue.popleft()
                if currentNode is not None:
                    if isNull or isNullAbove:
                        return False
                    queue.append(currentNode.left)
                    queue.append(currentNode.right)
                else:
                    isNull= True
            # in case there's one more deep level and the last node from the current level was Null
            isNullAbove = isNull
        return True

'''
    For a complete binary tree, there should not be any node after we met an empty one.
'''