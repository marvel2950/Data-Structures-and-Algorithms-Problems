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

    def length(self):
        cur = self.head 
        len = 0
        while cur!=None:
            len=len+1 
            cur = cur.next
        return len

l = LinkedList()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    l.insertAtStart(i)

len = l.length()
print(len)