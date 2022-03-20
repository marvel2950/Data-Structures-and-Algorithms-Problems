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

    def print(self):
        for i in self.q:
            print(i,end=" ")
        print()

q = Queue()
q.enque(5)
q.enque(6)
q.enque(7)
q.enque(8)
q.print()
q.deque()
q.deque()
q.print()