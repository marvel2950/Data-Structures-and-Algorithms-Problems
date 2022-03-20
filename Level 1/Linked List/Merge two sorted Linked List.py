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

def mergeList(head1,head2):
    sorted_list = LinkedList()
    if head1==None:
        sorted_list.head = head2
    elif head2==None:
        sorted_list.head = head1 
    else:
        if head1.val <= head2.val:
            sorted_list.head= head1 
            head1 = head1.next
        else:
            sorted_list.head= head2
            head2 = head2.next 
    
    temp_head = sorted_list.head 

    while head1 and head2:
        if head1.val<=head2.val:
            temp_head.next = head1 
            temp_head = temp_head.next 
            head1 = head1.next
        else:
            temp_head.next = head2 
            temp_head = temp_head.next 
            head2 = head2.next

    if head1==None:
        temp_head.next = head2 
    if head2==None:
        temp_head.next =head1 
    
    return sorted_list


list1 = LinkedList()
nodes_val_1 = [1,5,8,12]
for val in nodes_val_1:
    list1.insertAtEnd(val)

list2 = LinkedList()
nodes_val_2 = [3,4,9,19]
for val in nodes_val_2:
    list2.insertAtEnd(val)
list1.print()
list2.print()

sorted_list = mergeList(list1.head,list2.head)
sorted_list.print()