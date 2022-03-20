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
        elif self.heap[index][0]<self.heap[parent][0]:
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
        if len(self.heap)>left and self.heap[smallest][0]>self.heap[left][0]:
            smallest = left
        if len(self.heap)>right and self.heap[smallest][0]>self.heap[right][0]:
            smallest = right
        if index!=smallest:
            self.__swap(index,smallest)
            self.__bubbleDown(smallest)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

def topKFrequent(arr,k):
    m = MinHeap()
    count = {}
    for i in arr:
        if i in count:
            count[i] = count[i]+1
        else:
            count[i] = 1
    
    for num,c in count.items():
        m.push([c,num])
        if len(m.heap)-1>k:
            m.pop()
    heap = m.heap[1:]
    l = []
    while len(heap)>0:
        l.append(heap[0][1])
        heap.pop(0)
    return l

arr = [1,1,1,1,1,2,2,2,3]
k = 2
topKArr = topKFrequent(arr,k)
print(topKArr)
