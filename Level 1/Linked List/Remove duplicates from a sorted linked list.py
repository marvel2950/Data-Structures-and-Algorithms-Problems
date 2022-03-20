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
    
    def removeDuplicates(self):
        cur = self.head 
        while cur and cur.next:
            if cur.val==cur.next.val:
                alpha = cur.next.next 
                cur.next = alpha 
            else:
                cur = cur.next


l = LinkedList()
nodes_val = [1,2,2,2,3,4,5,5,5,5]
for val in nodes_val:
    l.insertAtEnd(val)
l.print()
l.removeDuplicates()
l.print()