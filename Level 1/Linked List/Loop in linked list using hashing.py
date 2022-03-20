class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def checkLoop(self):
        hash = {}
        loopNode = None 
        cur = self.head 
        while cur!=None:
            if cur not in hash:
                hash[cur] = True 
            else:
                loopNode = cur 
                break 
            cur=cur.next
        return loopNode


l = LinkedList()
l.head = Node(5)
l.head.next = Node(1)
l.head.next.next = Node(6)
p = l.head.next.next
l.head.next.next.next = Node(7)
l.head.next.next.next.next = Node(8)
l.head.next.next.next.next.next = p

loopNode = l.checkLoop()
print(loopNode)
