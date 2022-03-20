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

    def evenOrOdd(self):
        cur = self.head
        state = None 
        while 1:
            if cur==None:
                state = "even"
                break
            elif cur.next == None:
                state = "odd"
                break
            cur = cur.next.next 
        return state

l = LinkedList()
nodes_val = [1,2,3,4]
for val in nodes_val:
    l.insertAtEnd(val)
l.print()
state = l.evenOrOdd()
print(state)
