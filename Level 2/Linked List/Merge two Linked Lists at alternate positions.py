class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,data):
        cur = self.head 
        newNode = Node(data)
        if cur==None:
            self.head = newNode
        else:
            while cur.next!=None:
                cur = cur.next 
            cur.next = newNode

def printList(head):
    cur = head 
    while cur!=None:
        print(cur.val,end=" ")
        cur = cur.next
    print()

def merge(h1,h2):
    p = h1 
    q = h2 
    while p!=None and q!=None:
        pNext = p.next 
        qNext = q.next 
        q.next = pNext 
        p.next = q 

        p = pNext
        q = qNext
    return h1


l1 = LinkedList()
nodes_val = [1,2,3,4,5]
for val in nodes_val:
    l1.insertAtEnd(val)
printList(l1.head)

l2 = LinkedList()
nodes_val = [6,7,8,9,10]
for val in nodes_val:
    l2.insertAtEnd(val)
printList(l2.head)

newHead = merge(l1.head,l2.head)
printList(newHead)