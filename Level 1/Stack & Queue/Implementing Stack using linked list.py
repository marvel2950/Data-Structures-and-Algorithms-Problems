class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None 

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.top 
        self.top = newNode

    def pop(self):
        if self.top == None:
            return None 
        else:
            popNode = self.top 
            self.top = self.top.next 
            return popNode

    def print(self):
        t = self.top
        while t!=None:
            print(t.val,end=" ")
            t = t.next 
        print()

s = Stack()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    s.push(i)
s.print()
print(s.pop().val)
s.print()