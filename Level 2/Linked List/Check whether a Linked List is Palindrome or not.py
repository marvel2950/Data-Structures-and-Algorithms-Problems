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

def pal1(head):
    st = []
    cur = head 
    while cur!=None:
        st.append(cur.val)
        cur = cur.next
    cur = head 
    while cur!=None:
        if cur.val != st.pop(-1):
            return False
        cur = cur.next
    return True

def reverse(head):
    cur = head 
    next,prev = None, None
    while cur!=None:
        next = cur.next 
        cur.next = prev 
        prev = cur 
        cur = next 
    head = prev
    return head

def pal2(head):
    head = copy.deepcopy(head)
    head1,head2 = split(head)
    # printList(head1)
    # printList(head2)
    head2 = reverse(head2)
    # printList(head1)
    # printList(head2)
    while head1!=None:
        if head1.val != head2.val:
            return False
        head1 = head1.next 
        head2 = head2.next
    return True

l = LinkedList()
nodes_val = [1,2,3,2,51]
for val in nodes_val:
    l.insertAtEnd(val)
l.print()

head = copy.deepcopy(l.head)

flag = pal1(head)
print(flag)


flag = pal2(head)
print(flag)
