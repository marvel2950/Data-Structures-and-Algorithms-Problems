class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.last = None
    
    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.last==None:
            self.last = newNode
            newNode.next = self.last
        else:
            newNode.next = self.last.next
            self.last.next = newNode
            self.last = newNode
            
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

l = LinkedList()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    l.insertAtEnd(i)
    l.print()