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

    def count(self):
        hash = {}
        cur = self.head
        while cur!=None:
            if cur.val not in hash:
                hash[cur.val] = 1
            else:
                hash[cur.val] = hash[cur.val]+1
            cur = cur.next
        return hash

l = LinkedList()
nodes_val = [1,2,2,1,5,7,4,3,4,5]
for val in nodes_val:
    l.insertAtEnd(val)
l.print()
countDict = l.count()
for key,value in countDict.items():
    print("Count of element",key,"is",value)