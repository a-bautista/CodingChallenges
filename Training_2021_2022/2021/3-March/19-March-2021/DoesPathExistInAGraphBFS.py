from collections import defaultdict, deque

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		
	def add_edge(self, start, end):
		self.graph[start].append(end)
		
	def does_path_exist(self, source, dest):
		
		visited = set()
		visited.add(source)
		queue = deque()
		queue.append(source)
		
		
		while queue:
			vertex = queue.popleft()
		
			# nodes contains the adjacent lists with the nodes
			nodes  = self.graph[vertex]
			
			if vertex == dest:
				return True

			while nodes:
				# get the current node
				currentNode = nodes.pop()
				
				if currentNode not in visited:
					
					queue.append(currentNode)
					visited.add(currentNode)
		return False

def main():
    g1 = Graph()
    g1.add_edge(0, 2)
    g1.add_edge(0, 5)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(5, 3)
    g1.add_edge(5, 6)
    g1.add_edge(3, 6)
    g1.add_edge(6, 7)
    g1.add_edge(6, 8)
    g1.add_edge(6, 4)
    g1.add_edge(7, 8)
    res = g1.does_path_exist(7, 8)
    print(res)

    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(0, 4)
    g2.add_edge(1, 5)
    g2.add_edge(4, 7)
    g2.add_edge(4, 8)
    res2 = g2.does_path_exist(0, 11)
    print(res2)

main()