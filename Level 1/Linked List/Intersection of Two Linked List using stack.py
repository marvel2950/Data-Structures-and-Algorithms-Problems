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

def intersectionPoint(h1,h2):
    interNode = None
    cur1 = h1 
    cur2 = h2 
    st1 = []
    st2 = []
    while cur1!=None:
        st1.append(cur1)
        cur1 = cur1.next
    while cur2!=None:
        st2.append(cur2)
        cur2 = cur2.next

    while len(st1) and len(st2) :
        alpha = st1.pop(-1)
        beta = st2.pop(-1)
        if alpha == beta:
            interNode = alpha 
    return interNode


l1 = LinkedList()
l1.head = Node(1)
l1.head.next = Node(2)
l1.head.next.next = Node(3)
p = l1.head.next.next
l1.head.next.next.next = Node(4)
l1.head.next.next.next.next = Node(5)
l1.print()

l2 = LinkedList()
l2.head = Node(11)
l2.head.next = Node(12)
l2.head.next.next = Node(13)
l2.head.next.next.next = Node(14)
l2.head.next.next.next.next = p
l2.print()

interNode = intersectionPoint(l1.head,l2.head)
print(interNode.val)