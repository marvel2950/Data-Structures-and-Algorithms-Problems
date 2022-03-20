class Stack:
    def __init__(self):
        self.st = []
    
    def push(self,data):
        self.st.append(data)

    def pop(self):
        popEle = -1
        if len(self.st)>0:
            popEle = self.st.pop(-1)
        return popEle

#Enque operation is costly.
class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enque(self,data):
        while len(self.s1.st)>0:
            alpha = self.s1.pop()
            self.s2.push(alpha)
        self.s1.push(data)
        while len(self.s2.st)>0:
            alpha = self.s2.pop()
            self.s1.push(alpha)

    def deque(self):
        if len(self.s1.st)==0:
            return None 
        else:
            popNode = self.s1.pop()
            return popNode

q = Queue()
q.enque(5)
q.enque(6)
q.enque(7)
print(q.deque())
print(q.deque())


#Deque operation is costly.
class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enque(self,data):
        self.s1.push(data)
        
    def deque(self):
        if len(self.s1.st)==0 and len(self.s2.st)==0:
            return None 
        else:
            if len(self.s2.st)==0:
                while len(self.s1.st)>0:
                    alpha = self.s1.pop()
                    self.s2.push(alpha)
            popNode = self.s2.pop()
            return popNode

q = Queue()
q.enque(5)
q.enque(6)
q.enque(7)
print(q.deque())
print(q.deque())