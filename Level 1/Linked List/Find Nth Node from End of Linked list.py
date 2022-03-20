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

    def nthNodeFromEnd(self,n):
        if self.head==None:
            return None
        ahead = self.head 
        behind = self.head 
        while ahead!=None and n-1>0:
            ahead = ahead.next
            n=n-1
        if ahead==None:
            return None
        while ahead.next!=None:
            ahead = ahead.next
            behind = behind.next
        return behind

l = LinkedList()
nodes_val = [1,2,3,4,5]
for val in nodes_val:
    l.insertAtEnd(val)
l.print()
n = 9
nthNode = l.nthNodeFromEnd(n)
print(nthNode)