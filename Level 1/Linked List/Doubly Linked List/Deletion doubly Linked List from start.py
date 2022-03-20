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
            
    def deleteAtStart(self):
        if self.head==None:
            return None 
        else:
            self.head = self.head.next 
            self.head.prev = None

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
l.print() #-> 5 4 3 2 1 
l.deleteAtStart()
l.print() #=> 4 3 2 1
l.deleteAtStart()
l.print() #=> 3 2 1