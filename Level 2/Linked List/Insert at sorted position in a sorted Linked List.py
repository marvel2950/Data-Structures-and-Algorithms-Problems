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

    def insertInSorted(self,key):
        cur = self.head 
        pos = None
        while cur!=None:
            if cur.val > key:
                break 
            pos = cur 
            cur = cur.next 
        if pos==None:
            temp = cur 
            self.head = Node(key)
            self.head.next = temp
        else:
            temp = pos.next 
            pos.next = Node(key)
            pos.next.next = temp

l = LinkedList()
nodes_val = [1,2,3,7,9,11]
for val in nodes_val:
    l.insertAtEnd(val)
l.print()

key = 5
l.insertInSorted(key)

l.print()