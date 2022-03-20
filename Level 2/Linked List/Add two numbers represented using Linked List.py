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

def add(l1,l2):
    head = Node(-1)
    headTemp = head 
    carry = 0
    while l1!=None and l2!=None:
        sum_val = l1.val+l2.val+carry 
        if sum_val>9:
            carry = sum_val//10
            sum_val = sum_val%10
        else:
            carry = 0
        head.next = Node(sum_val)
        head = head.next
        l1 = l1.next 
        l2 = l2.next
    if l1==None and l2==None:
        pass
    elif l1==None:
        while l2!=None:
            sum_val = l2.val+carry 
            if sum_val>9:
                carry = sum_val//10
                sum_val = sum_val%10
            else:
                carry = 0
            head.next = Node(sum_val)
            head = head.next
            l2 = l2.next
    elif l2==None:
        while l1!=None:
            sum_val = l1.val+carry 
            if sum_val>9:
                carry = sum_val//10
                sum_val = sum_val%10
            else:
                carry = 0
            head.next = Node(sum_val)
            head = head.next
            l1 = l1.next
    if carry>0:
        head.next = Node(carry)
    return headTemp.next

l1 = LinkedList()
nodes_val = [4,3,2] #=> 234
for val in nodes_val:
    l1.insertAtEnd(val)
printList(l1.head)

l2 = LinkedList()
nodes_val = [5,6] #=> 65
for val in nodes_val:
    l2.insertAtEnd(val)
printList(l2.head)
head = add(l1.head,l2.head)
printList(head) #=> 299

