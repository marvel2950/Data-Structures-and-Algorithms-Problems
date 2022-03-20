class MaxHeap:
    def __init__(self,items=[]):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)

    def __floatUp(self,index):
        parent = index//2 
        if index<=1:
            return 
        elif self.heap[index]>self.heap[parent]:
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
        largest = index 
        if len(self.heap)>left and self.heap[largest]<self.heap[left]:
            largest = left
        if len(self.heap)>right and self.heap[largest]<self.heap[right]:
            largest = right
        if index!=largest:
            self.__swap(index,largest)
            self.__bubbleDown(largest)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

def kClosest(arr,k,x):
    m = MaxHeap()
    map = {}
    for i in arr:
        m.push(abs(i-x))
        alpha = abs(i-x)
        if alpha in map:
            map[alpha].append(i)
        else:
            map[alpha] = [i]
        if len(m.heap)-1>k:
            m.pop()
    print(map)
    heap = list(set(m.heap[1:]))
    print(heap)
    l = []
    while len(heap)>0:
        l.extend(map[heap[0]])
        heap.pop(0)
    return l

arr = [5,4,1,2,8,3]
k = 3
x = 4
arrClosest = kClosest(arr,k,x)
print(arrClosest)
