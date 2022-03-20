class Node:
	def __init__(self,freq,symbol,left=None,right=None):
		self.huff = ''
		self.freq = freq
		self.symbol = symbol
		self.left = left
		self.right = right

def printNodes(node,val=''):
	newVal = val + node.huff
	if node.left:
		printNodes(node.left,newVal)
	if node.right:
		printNodes(node.right,newVal)

	if node.left==None and node.right == None:
		print(node.symbol,newVal)
	

chars = ['a','b','c','d','e','f']
freq = [5,9,12,13,16,45]

nodes = []
for x in range(len(chars)):
	nodes.append(Node(freq[x],chars[x]))

while len(nodes)>1:
	nodes = sorted(nodes,key=lambda x:x.freq)
	left = nodes.pop(0)
	right = nodes.pop(0)
	left.huff = '0'
	right.huff = '1'
	newNode = Node(
		left.freq+right.freq,
		left.symbol+right.symbol,
		left,
		right 
	)
	nodes.append(newNode)
printNodes(nodes[0])