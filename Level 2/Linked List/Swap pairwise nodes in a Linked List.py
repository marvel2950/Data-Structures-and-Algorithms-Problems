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
    if p==None:
        return None 
    while p!=None:
        if p.next==None:
            break
        p.val, p.next.val = p.next.val, p.val
        p = p.next.next
    return head


l = LinkedList()
nodes_val = [1]
for val in nodes_val:
    l.insertAtEnd(val)
printList(l.head)
newHead = swapNodes(l.head)
printList(newHead)