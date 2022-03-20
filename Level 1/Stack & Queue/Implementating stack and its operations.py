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

    def print(self):
        for i in range(len(self.st)-1,-1,-1):
            print(self.st[i],end= " ")
        print()

s = Stack()
values = [1,2,3,4,5]
for i in values:
    s.push(i)
s.print()
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

s.print()