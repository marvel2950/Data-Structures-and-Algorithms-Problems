class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 

    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while 1:
                if data<cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        break
                elif data>cur.val:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        break 
                else:
                    break

def levelOrder(root):
    traversal = []    
    row = []
    q = [root,None]
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
                traversal.append(row)
            row = []
        if p==None and prev==None:
            break 
        prev = p
    return traversal

tree = BinarySearchTree()
nodes = [6,8,7,9,4,3,5]
for i in nodes:
    tree.insert(i)

traversal = levelOrder(tree.root)
for row in traversal:
    print(*row)