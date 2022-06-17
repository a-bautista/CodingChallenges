class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
def solve(root,p):
	queue = deque()
	res = []
	count = 0
	flag = 0
	queue.append(root)
	while queue:
		level = len(queue)
		count+=1
		for _ in range(level):
			currentNode = queue.popleft()
			res.append(currentNode.val)
			if currentNode.val== p:
				flag = count
			if currentNode.left:
				queue.append(currentNode.left)
			if currentNode.right:
				queue.append(currentNode.right)
				
	for i in range(len(res)):
		if i == flag:
			return res[i+1]
	return -1

def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.right = Node(3)
    root.left.right = Node(5)
    res = solve(root, 3)
    print(res)

main()
