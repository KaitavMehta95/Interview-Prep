import sys # Library for INT_MAX 
class Graph():
	def __init__(self,vertices):

		self.V =vertices
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

		print(self.graph)

# Loops over all the nodes to find the min value node which is not explored
	def minNode(self,values,mst):
#  TODO : Improve by using heaps
		min = sys.maxsize
		for v in range(self.V):
			if values[v] < min and mst[v] == False:
				min= values[v]
				min_index= v

		return min_index



	def primMST(self):
		values = [sys.maxsize] * self.V
		parent = [None]*self.V
		values[0] = 0
		mst= [False]*self.V

# First node is always at root
		parent[0] = -1



		for node in range(self.V):
			u = self.minNode(values,mst)
			mst[u] = True

			for v in range(self.V):
				if self.graph[u][v] > 0 and values[v] > self.graph[u][v] and mst[v] == False:
					values[v] = self.graph[u][v]
					parent[v] = u


		print("Edge  Weight")
		for i in range(1, self.V): 
			print(parent[i], "-", i, "\t", self.graph[i][ parent[i] ]) 



g = Graph(5)

g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 

g.primMST()
