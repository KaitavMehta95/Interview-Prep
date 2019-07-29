from collections import defaultdict

class Graph:

	#Constructor
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)


	def dfsRecursion(self,v,visited):
		visited[v] = True
		print(v)

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]== False:
				self.dfsRecursion(i,visited)


	def dfs(self,v):
		visited= [False]*(len(self.graph))
		self.dfsRecursion(v,visited)



	def bfs(self,v):
		visited = [False]*(len(self.graph))
		# Create a queue for BFS
		queue=[]

		queue.append(v)
		visited[v] = True

		while queue:

			v = queue.pop(0)
			print(v)

			for i in self.graph[v]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True				




g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)


# g.dfs(2)

g.bfs(2)
