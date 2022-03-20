class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        cur = self.head 
        while cur!=None:
            print(cur.val,end=" ")
            cur = cur.next
        print()

    def insertAtEnd(self,data):
        cur = self.head 
        newNode = Node(data)
        if cur==None:
            self.head = newNode
        else:
            while cur.next!=None:
                cur = cur.next 
            cur.next = newNode

    def search(self,key):
        cur = self.head 
        keyNode = None 
        while cur!=None:
            if cur.val==key:
                keyNode = cur
                break 
            cur = cur.next 
        return keyNode

    def insertAtMiddle(self,data,pos):
        newNode = Node(data)
        store = pos.next
        pos.next = newNode 
        newNode.next = store

    def deleteAtMiddle(self,pos):
        cur = self.head 
        if cur==pos or cur==None:
            self.head = None
        else:
            prev = None
            while cur!=pos:
                prev = cur
                cur = cur.next 
            prev.next = cur.next


l = LinkedList()
nodes_val = [1,2,3,4,5]
for val in nodes_val:
    l.insertAtEnd(val)
l.print() # => 1 2 3 4 5 
posValue = 3
posNode = l.search(posValue)
data = 10
l.insertAtMiddle(data,posNode)
l.print() #=> 1 2 3 10 4 5
l.deleteAtMiddle(posNode)
l.print() #=> 1 2 10 4 5