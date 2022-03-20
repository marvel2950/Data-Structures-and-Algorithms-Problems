from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def BFS(self,s,visited):
		queue = []
		queue.append(s)
		visited[s]= True
		while len(queue)!=0:
			s = queue.pop(0)
			print(s,end=" ")
			for i in self.graph[s]:
				if visited[i]==False:
					queue.append(i)
					visited[i] = True
	
	def BFS_disconnected(self):
		visited = [False]*(max(self.graph)+1)
		for i in self.graph.keys():
			if not visited[i]:
				self.BFS(i,visited)




g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(4,5)
g.addEdge(6,7)
g.BFS_disconnected()