import copy
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

def printList(head):
    cur = head 
    while cur!=None:
        print(cur.val,end=" ")
        cur = cur.next
    print()

def split(head):
    p = head 
    q = head
    head1 = p
    while 1:
        p = p.next.next 
        #even 
        if p == None:
            head2 = q.next
            break
        #odd
        if p.next == None:
            head2 = q.next.next 
            break 
        
        q = q.next 
    q.next = None 
    return [head1,head2]

l = LinkedList()
nodes_val = [1,2,3,4]
for val in nodes_val:
    l.insertAtEnd(val)
l.print()

head = copy.deepcopy(l.head)
head1,head2 = split(head)
printList(l.head)
printList(head1)
printList(head2)