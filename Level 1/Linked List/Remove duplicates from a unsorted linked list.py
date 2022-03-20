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


    def removeDuplicates(self):
        hash = {}
        cur = self.head
        while cur!=None:
            if cur.val not in hash:
                hash[cur.val] = True 
            else:
                self.deleteAtMiddle(cur)
            cur = cur.next

l = LinkedList()
nodes_val = [4,1,2,3,4,2,5]
for val in nodes_val:
    l.insertAtEnd(val)
l.print()
l.removeDuplicates()
l.print()