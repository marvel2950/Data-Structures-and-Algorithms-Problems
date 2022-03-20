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

def sortedOrNot(head):
    if head==None or head.next == None:
        return True 
    return head.val <head.next.val and sortedOrNot(head.next)

def sortedOrNot2(head):
    if head==None or head.next == None:
        return True 
    prev = head 
    cur = head.next 
    while cur!=None:
        if prev.val > cur.val:
            return False 
        prev = cur 
        cur = cur.next
    return True

l = LinkedList()
nodes_val = [1,2,3,4,5]
for val in nodes_val:
    l.insertAtEnd(val)
l.print()

flag = sortedOrNot(l.head)
print(flag)

flag = sortedOrNot2(l.head)
print(flag)