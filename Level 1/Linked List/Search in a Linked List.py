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

    def search(self,key):
        cur = self.head
        keyNode = None
        while cur!=None:
            if cur.val == key:
                keyNode = cur
                break 
            cur=cur.next
        return keyNode

l = LinkedList()
nodes_val = [1,2,3,4,5]
for i in nodes_val:
    l.insertAtStart(i)

key = 3
keyNode = l.search(key)
print(keyNode.val)