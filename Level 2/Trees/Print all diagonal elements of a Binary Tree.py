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

def diagonalElements(root):
    q = [root]
    hash = {}
    hash[0] = [root.val]
    root.val = [root.val,0]
    traversal = []

    while q!=[]:
        p = q.pop(0)
        if p:
            if p.left:
                q.append(p.left)
                depth = p.val[1]-1
                if depth in hash:
                    hash[depth].append(p.left.val)
                else:
                    hash[depth] = [p.left.val]
                p.left.val = [p.left.val,depth]
            if p.right:
                q.append(p.right)
                depth = p.val[1]
                if depth in hash:
                    hash[depth].append(p.right.val)
                else:
                    hash[depth] = [p.right.val]
                p.right.val = [p.right.val,depth]
    
    for i,j in hash.items():
        traversal.append(j)
    return traversal

def diagonalElements(root):
    q = [root,None]
    row = []
    traversal = []

    while q!=[]:
        p = q.pop(0)
        if p==None:
            q.append(None)
            p = q.pop(0)
            if p==None:
                break 

        while p!=None:
            row.append(p.val)
            if p.left:
                q.append(p.left)
            p = p.right 
        traversal.append(row)
        row = []
        
    return traversal
    
tree = BinarySearchTree()
nodes = [6,8,7,9,4,3,5]
for i in nodes:
    tree.insert(i)

traversal = diagonalElements(tree.root)
for row in traversal:
    print(*row)