class Node:
    def __init__ (self,data):
        self.val = data 
        self.left = None
        self.right = None

def zigzagTraversal(root):
    traversal = []
    stack1 = [root]
    stack2 = []
    row = []
    traversal = []
    while len(stack1)!=0 or len(stack2)!=0:
        while len(stack1)!=0:
            p = stack1.pop(-1)
            #print(p.val,end=" ")
            row.append(p.val)
            if p.left:
                stack2.append(p.left)
            if p.right:
                stack2.append(p.right)
        if len(row)!=0:
            traversal.append(row)
        row = []

        while len(stack2)!=0:
            p = stack2.pop(-1)
            #print(p.val,end=" ")
            row.append(p.val)
            if p.right:
                stack1.append(p.right)
            if p.left:
                stack1.append(p.left)
        if len(row)!=0:
            traversal.append(row)
        row = []
    return traversal 

def zigzagTraversal(root):
    traversal = []    
    row = []
    q = [root,None]
    flag = False
    prev = None
    while len(q)!=0:
        p = q.pop(0)
        if p:
            row.append(p.val)
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        else:
            q.append(None)
            if row!=[]:
                if flag==False:
                    traversal.append(row)
                    flag = True
                else:
                    traversal.append(row[::-1])
                    flag = False

            row = []
        if p==None and prev==None:
            break 
        prev = p
    return traversal

tree = Node(6)
tree.left = Node(4)
tree.right = Node(8)     
tree.left.left = Node(3)
p = tree.left.right = Node(5)     
q = tree.right.left = Node(7)
tree.right.right = Node(9)     

traversal = zigzagTraversal(tree)
# print(traversal)
for row in traversal:
    print(*row)
