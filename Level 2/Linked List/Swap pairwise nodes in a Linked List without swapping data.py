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

def swapNodes(head):
    p = head 
    if p==None or p.next == None:
        return head
    newHead = p.next 
    while 1:
        q = p.next 
        temp = q.next 
        q.next = p
        if temp==None or temp.next==None:
            p.next = temp 
            break 
        p.next = temp.next 
        p = temp
    return newHead


l = LinkedList()
nodes_val = [1,2,3,4,5]
for val in nodes_val:
    l.insertAtEnd(val)
printList(l.head)
newHead = swapNodes(l.head)
printList(newHead)