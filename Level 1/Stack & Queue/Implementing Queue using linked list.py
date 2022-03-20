class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None

    def enqueue(self,data):
        newNode = Node(data)
        if self.rear == None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode 
            self.rear = newNode

    def dequeue(self):
        if self.front == None:
            return None 
        else:
            popNode = self.front
            self.front = self.front.next 
            if self.front == None:
                self.rear = None
            return popNode

    def print(self):
        t = self.front
        while t!=None:
            print(t.val,end=" ")
            t = t.next 
        print()

q = Queue()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    q.enqueue(i)
q.print()
print(q.dequeue().val)
q.print()