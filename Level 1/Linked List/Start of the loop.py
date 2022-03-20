class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def checkLoop(self):
        loopNode = None 
        slow = self.head
        fast = self.head 
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow==fast:
                loopNode = slow 
                break
        return loopNode

    def startLoop(self):
        p = self.head
        q = self.checkLoop()
        while p!=q:
            p=p.next
            q = q.next 
        return p


l = LinkedList()
l.head = Node(5)
l.head.next = Node(1)
l.head.next.next = Node(6)
p = l.head.next.next
l.head.next.next.next = Node(7)
l.head.next.next.next.next = Node(8)
l.head.next.next.next.next = p

loopNode = l.checkLoop()
loopStartNode = l.startLoop()
print(loopStartNode.val)
