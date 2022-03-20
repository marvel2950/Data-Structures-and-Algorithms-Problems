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

    def length(self):
        cur = self.head 
        len = 0
        while cur!=None:
            len=len+1 
            cur = cur.next
        return len

def intersectionPoint(l1,l2):
    interNode = None
    cur1 = l1.head
    cur2 = l2.head
    len1 = l1.length()
    len2 = l2.length()
    if len1>len2:
        d = len1-len2
        while cur1!=None and d>0:
            cur1 = cur1.next
            d = d-1
    else:
        d = len2-len1
        while cur2!=None and d>0:
            cur2 = cur2.next
            d = d-1

    while cur1!=cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    interNode = cur1
    return interNode


l1 = LinkedList()
l1.head = Node(1)
l1.head.next = Node(2)
l1.head.next.next = Node(3)
p = l1.head.next.next
l1.head.next.next.next = Node(4)
l1.head.next.next.next.next = Node(5)
l1.print() #=> 1 2 3 4 5 

l2 = LinkedList()
l2.head = Node(11)
l2.head.next = Node(12)
l2.head.next.next = Node(13)
l2.head.next.next.next = Node(14)
l2.head.next.next.next.next = p
l2.print() #=> 11 12 13 14 3 4 5

interNode = intersectionPoint(l1,l2)
print(interNode.val)