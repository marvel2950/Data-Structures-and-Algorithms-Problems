from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def DFS(self,s):
		visited = [False]*(max(self.graph)+1)
		stack = []
		stack.append(s)
		while stack:
			s = stack.pop(-1)
			if visited[s]==False:
				print(s,end=" ")
				visited[s] = True 
			for i in self.graph[s]:
				if visited[i]==False:
					stack.append(i)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS(0)