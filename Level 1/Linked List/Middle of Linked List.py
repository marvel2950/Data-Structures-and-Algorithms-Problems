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

    def insertAtEnd(self,data):
        cur = self.head 
        newNode = Node(data)
        if cur==None:
            self.head = newNode
        else:
            while cur.next!=None:
                cur = cur.next 
            cur.next = newNode

    def middleElement1(self):
        len = l.length()
        mid = len//2
        cur = self.head 
        pos = 0
        while pos!=mid:
            cur=cur.next
            pos=pos+1 
        return cur
        
    def middleElement2(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

l = LinkedList()
nodes_val = [1,2,3,4,5,6]
for val in nodes_val:
    l.insertAtEnd(val)
l.print() #=> 1 2 3 4 5 6
middleEle1 = l.middleElement1()
print(middleEle1.val) #=> 4
middleEle2 = l.middleElement2()
print(middleEle2.val) #=> 4