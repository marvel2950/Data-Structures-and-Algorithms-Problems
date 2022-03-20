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

    def search(self,key):
        cur = self.head 
        keyNode = None 
        while cur!=None:
            if cur.val == key:
                keyNode = cur 
                break
            cur = cur.next 
        return keyNode

    def deleteAtMiddle(self,pos):
        cur = self.head 
        if cur==None or cur==pos:
            return None
        prev = pos.prev
        prev.next = pos.next 
        pos.next.prev = pos

l = LinkedList()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    l.insertAtStart(i)
l.print() #=> 5 4 3 2 1 
posValue = 3
posNode = l.search(posValue)
l.deleteAtMiddle(posNode)
l.print() #=> 5 4 2 1 