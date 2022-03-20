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
        elif self.heap[index]<self.heap[parent]:
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
        if len(self.heap)>left and self.heap[smallest]>self.heap[left]:
            smallest = left
        if len(self.heap)>right and self.heap[smallest]>self.heap[right]:
            smallest = right
        if index!=smallest:
            self.__swap(index,smallest)
            self.__bubbleDown(smallest)

def connectRopes(arr):
    cost = 0
    m = MinHeap(arr)
    while len(m.heap)-1>=2:
        alpha = m.pop()
        beta = m.pop()
        newRope = alpha+beta 
        cost=cost+newRope
        m.push(newRope)
    return cost

arr = [1,2,3,4,5]
cost = connectRopes(arr)
print(cost)