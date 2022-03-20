#1st approach
from collections import defaultdict


edges = [[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]]
graph = {}
for i,j in edges:
	if i in graph:
		graph[i].append(j)
	else:
		graph[i] = [j]
print(graph)

#2nd approach
edges = [[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]]
graph = defaultdict(list)
for i,j in edges:
	graph[i].append(j)
print(dict(graph))

#3rd approach
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	
	def addEdge(self,u,v):
		self.graph[u].append(v)

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print(dict(g.graph))

g1 = Graph()
g1.addEdge(0,1)
g1.addEdge(0,2)
g1.addEdge(1,2)
g1.addEdge(2,0)
print(dict(g1.graph))

#4th approach
edges = [[0,1],[0,2],[1,2],[2,0],[2,3],[3,3]]
graph = []
n = 3
for _ in range(4):
	row = []
	for __ in range(4):
		row.append(0)
	graph.append(row)
for i,j in edges:
	graph[i][j] = 1
for i in graph:
	print(i)