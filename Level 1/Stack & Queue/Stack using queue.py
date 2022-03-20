
class Queue:
    def __init__(self):
        self.q = []
    
    def enque(self,data):
        self.q.append(data)

    def deque(self):
        popEle = -1
        if len(self.q)>0:
            popEle = self.q.pop(0)
        return popEle

#Push operation is costly.
class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self,data):
        self.q2.enque(data)
        while len(self.q1.q)>0:
            alpha = self.q1.deque()
            self.q2.enque(alpha)
        self.q1,self.q2 = self.q2,self.q1

    def pop(self):
        if len(self.q1.q)==0:
            return None
        else:
            popNode = self.q1.deque()
            return popNode

    def print(self):
        for i in self.q1.q:
            print(i,end=" ")
        print()


s = Stack()
values = [1,2,3,4,5]
for i in values:
    s.push(i)
s.print()
print(s.pop())
print(s.pop())
s.print()



#Pop operation is costly.
class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self,data):
        self.q1.enque(data)
        
    def pop(self):
        if len(self.q1.q)==0:
            return None
        else:
            while len(self.q1.q)>1:
                alpha = self.q1.deque()
                self.q2.enque(alpha)
            popNode = self.q1.deque()
            self.q1,self.q2 = self.q2,self.q1
            return popNode

    def print(self):
        for i in self.q1.q:
            print(i,end=" ")
        print()


s = Stack()
values = [1,2,3,4,5]
for i in values:
    s.push(i)
s.print()
print(s.pop())
print(s.pop())
s.print()
print(s.pop())


