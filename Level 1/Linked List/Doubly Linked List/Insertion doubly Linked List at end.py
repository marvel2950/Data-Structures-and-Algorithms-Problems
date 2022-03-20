class Node:
    def __init__(self,data):
        self.val = data
        self.next = None 
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def insertAtEnd(self,data):
        cur = self.head
        newNode = Node(data)
        if self.head==None:
            self.head = newNode 
        else:
            while cur.next!=None:
                cur = cur.next 
            cur.next = newNode
            newNode.prev = cur

    def print(self):
        cur = self.head 
        while cur!=None:
            print(cur.val,end=" ")
            cur = cur.next
        print()

l = LinkedList()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    l.insertAtEnd(i)

l.print()