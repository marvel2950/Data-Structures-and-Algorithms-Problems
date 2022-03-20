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

def insertAtSortedPos(nodes,newNode):
	flag = 0
	for i in range(len(nodes)):
		if nodes[i].freq > newNode.freq:
			flag = 1
			nodes.insert(i,newNode)
			break
	if flag==0:
		nodes.append(newNode)
	
chars = ['a','b','c','d','e','f']
freq = [5,9,12,13,16,45]

nodes = []
for x in range(len(chars)):
	nodes.append(Node(freq[x],chars[x]))

while len(nodes)>1:
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
	# nodes.append(newNode)
	insertAtSortedPos(nodes,newNode)
printNodes(nodes[0])