class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		
class Solution:
	def solve(self, root):
		if root is not None:
			res = self.rec_helper(root)
			if res == 0:
				root = None
            return res
	
	
	def rec_helper(self, root):
	
		if root is None:
			return 0
			
		sumLeft = self.rec_helper(root.left)
		sumRight = self.rec_helper(root.right)
		
		if sumLeft == 0:
			root.left = None
			
		if sumRight == 0:
			root.right = None
			
		return root.val + sumLeft + sumRight
		
		
def main():
	root = Node(1)
	root.left = Node(7)
	root.right = Node(8)
	root.left.left = Node(-9)
	root.left.right = Node(2)

	
	solution = Solution()
	res = solution.solve(root)
	print(res)
	
main()