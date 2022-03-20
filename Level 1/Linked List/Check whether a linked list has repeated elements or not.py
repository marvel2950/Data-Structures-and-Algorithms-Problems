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

    def checkRepeated1(self):
        flag = False 
        cur1 = self.head 
        while cur1!=None:
            cur2 = self.head
            while cur2!=None:
                if cur1!=cur2 and cur1.val==cur2.val:
                    flag = True 
                    break 
                cur2=cur2.next
            cur1=cur1.next 
        return flag

    def checkRepeated2(self):
        flag = False 
        cur = self.head 
        hash = {}
        while cur!=None:
            if cur.val not in hash:
                hash[cur.val] = True 
            else:
                flag = True
                break
            cur=cur.next 
        return flag


l = LinkedList()
nodes_val = [1,2,3,4,5]
for val in nodes_val:
    l.insertAtEnd(val)
l.print()
flag1 = l.checkRepeated1()
print(flag1)
flag2 = l.checkRepeated1()
print(flag2)