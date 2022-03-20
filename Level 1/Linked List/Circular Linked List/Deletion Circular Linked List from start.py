class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.last = None
    
    def insertAtStart(self,data):
        newNode = Node(data)
        if self.last==None:
            self.last = newNode
            newNode.next = self.last
        else:
            newNode.next = self.last.next 
            self.last.next = newNode
    
    def print(self):
        if self.last==None:
            return None 
        cur = self.last.next

        while 1:
            print(cur.val,end=" ")
            if cur==self.last:
                break 
            cur = cur.next
        print()

    def deleteAtStart(self):
        if self.last==None:
            return None 
        if self.last.next == self.last:
            self.last=None 
        else:
            self.last.next = self.last.next.next

l = LinkedList()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    l.insertAtStart(i)
l.print() #=> 5 4 3 2 1 
l.deleteAtStart()
l.print() #=> 4 3 2 1
l.deleteAtStart()
l.print() #=> 3 2 1