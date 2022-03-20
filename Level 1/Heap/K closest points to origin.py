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
        elif self.heap[index][0]>self.heap[parent][0]:
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
        if len(self.heap)>left and self.heap[largest][0]<self.heap[left][0]:
            largest = left
        if len(self.heap)>right and self.heap[largest][0]<self.heap[right][0]:
            largest = right
        if index!=largest:
            self.__swap(index,largest)
            self.__bubbleDown(largest)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

def kClosestPoints(points,k):
    m = MaxHeap()
    for point in points:
        x = point[0]
        y = point[1]
        dist = (x**2+y**2)
        m.push([dist,point])
        if len(m.heap)-1>k:
            m.pop()
        ans = []
    for i in m.heap[1:]:
        ans.append(i[1])
    return ans

points = [[1,3],[-2,2],[-1,-1],[4,4]]
k = 2
ans = kClosestPoints(points,k)
print(ans)