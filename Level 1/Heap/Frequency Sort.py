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

def frequencySort(arr):
    m = MaxHeap()
    count = {}
    for i in arr:
        if i in count:
            count[i] = count[i]+1 
        else:
            count[i] = 1
    print(count)
    for num,c in count.items():
        m.push([c,num])
    ans = []
    while len(m.heap)>1:
        c = m.pop()
        for _ in range(c[0]):
            ans.append(c[1])
    return ans

arr = [1,1,1,2,2,2,2,2,2,1,1,1,1,1,4,3,4,3,4,3,4]
ans = frequencySort(arr)
print(ans)
