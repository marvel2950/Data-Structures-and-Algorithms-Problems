class Node:
    def __init__(self,data):
        self.val = data
        self.next = None 
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def insertAtStart(self,data):
        newNode = Node(data)
        if self.head==None:
            self.head = newNode 
        else:
            self.head.prev = newNode 
            newNode.next = self.head 
            self.head = newNode

    def print(self):
        cur = self.head 
        while cur!=None:
            print(cur.val,end=" ")
            cur = cur.next
        print()

l = LinkedList()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    l.insertAtStart(i)

print(l.head.val)
l.print()