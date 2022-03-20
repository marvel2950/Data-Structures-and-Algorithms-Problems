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

    def search(self,key):
        cur = self.head
        keyNode = None
        while cur!=None:
            if cur.val == key:
                keyNode = cur
                break 
            cur=cur.next
        return keyNode

def printList(head):
    cur = head 
    while cur!=None:
        print(cur.val,end=" ")
        cur = cur.next
    print()

def rotate(head,rNode):
    p = head
    while p!=None:
        if p==rNode:
            break
        p = p.next
    newHead = p.next
    p.next = None
    q = newHead
    while q.next!=None:
        q = q.next 
    q.next = head 
    return newHead

l = LinkedList()
nodes_val = [1,2,3,4,5]
for val in nodes_val:
    l.insertAtEnd(val)
printList(l.head)
key = 3
keyNode = l.search(key)
newHead = rotate(l.head,keyNode)
printList(newHead)