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

    def search(self,key):
        if self.last==None:
            return None 
        cur = self.last.next
        keyNode = None

        while 1:
            if cur.val==key:
                keyNode = cur 
                break
            if cur==self.last:
                break 
            cur = cur.next
        return keyNode

    def insertAtMiddle(self,data,pos):
        newNode = Node(data)
        store = pos.next 
        pos.next = newNode
        newNode.next = store

    def deleteAtMiddle(self,pos):
        cur = self.last.next
        if self.last==None:
            return None 
        else:
            prev = None 
            while cur!=pos:
                prev = cur
                cur = cur.next
            prev.next = cur.next
            



l = LinkedList()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    l.insertAtStart(i)
l.print() #=> 5 4 3 2 1 
key = 3
posNode = l.search(key)
data = 10 
l.insertAtMiddle(data,posNode)
l.print() #=> 5 4 3 10 2 1
l.deleteAtMiddle(posNode)
l.print() #=> 5 4 10 2 1                                 