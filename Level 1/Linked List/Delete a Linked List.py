class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self,data):
        newNode = Node(data)
        newNode.next  =self.head
        self.head = newNode

    def delete(self):
        cur = self.head 
        while cur:
            prev = cur.next 
            del cur.val 
            cur = prev

l = LinkedList()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    l.insertAtStart(i)

