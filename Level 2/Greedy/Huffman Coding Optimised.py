class Node:
	def __init__(self,freq,symbol,left=None,right=None):
		self.huff = ''
		self.freq = freq
		self.symbol = symbol
		self.left = left
		self.right = right

class MinHeap:
    def __init__(self,items=[]):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)

    def __floatUp(self,index):
        parent = index//2 
        if index<=1:
            return 
        elif self.heap[index].freq<self.heap[parent].freq:
            self.__swap(index,parent)
            self.__floatUp(parent)

    def __swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

    def push(self,data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    def pop(self):
        if len(self.heap)>2:
            self.__swap(1,len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap)==2:
            max = self.heap.pop()
        else:
            max = False 
        return max 

    def __bubbleDown(self,index):
        left = index*2
        right = 2*index +1 
        smallest = index 
        if len(self.heap)>left and self.heap[smallest].freq>self.heap[left].freq:
            smallest = left
        if len(self.heap)>right and self.heap[smallest].freq>self.heap[right].freq:
            smallest = right
        if index!=smallest:
            self.__swap(index,smallest)
            self.__bubbleDown(smallest)

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

nodes = MinHeap()
for x in range(len(chars)):
	nodes.push(Node(freq[x],chars[x]))

while len(nodes.heap)-1>1:
	left = nodes.pop()
	right = nodes.pop()
	left.huff = '0'
	right.huff = '1'
	newNode = Node(
		left.freq+right.freq,
		left.symbol+right.symbol,
		left,
		right 
	)
	nodes.push(newNode)
printNodes(nodes.heap[1])
 